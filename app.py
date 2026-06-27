from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_connection, init_db
from werkzeug.security import generate_password_hash, check_password_hash
import qrcode
import io
import base64
import functools

app = Flask(__name__)
app.secret_key = 'mediplan-geheim-2026'

with app.app_context():
    init_db()

def login_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        if 'nutzer_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@login_required
def index():
    conn = get_connection()
    patienten = conn.execute('SELECT * FROM patienten WHERE nutzer_id = ?', (session['nutzer_id'],)).fetchall()
    conn.close()
    return render_template('index.html', patienten=patienten)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        passwort = request.form['passwort']
        conn = get_connection()
        existing = conn.execute('SELECT * FROM nutzer WHERE username = ?', (username,)).fetchone()
        if existing:
            flash('Benutzername bereits vergeben!', 'danger')
            return render_template('register.html')
        passwort_hash = generate_password_hash(passwort)
        conn.execute('INSERT INTO nutzer (username, passwort) VALUES (?, ?)', (username, passwort_hash))
        conn.commit()
        conn.close()
        flash('Registrierung erfolgreich! Bitte einloggen.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        passwort = request.form['passwort']
        conn = get_connection()
        nutzer = conn.execute('SELECT * FROM nutzer WHERE username = ?', (username,)).fetchone()
        conn.close()
        if nutzer and check_password_hash(nutzer['passwort'], passwort):
            session['nutzer_id'] = nutzer['id']
            session['username'] = nutzer['username']
            return redirect(url_for('index'))
        flash('Falscher Benutzername oder Passwort!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/patient/neu', methods=['GET', 'POST'])
@login_required
def patient_neu():
    if request.method == 'POST':
        name = request.form['name']
        geburtsdatum = request.form['geburtsdatum']
        allergien = request.form['allergien']
        conn = get_connection()
        conn.execute('INSERT INTO patienten (nutzer_id, name, geburtsdatum, allergien) VALUES (?, ?, ?, ?)',
                     (session['nutzer_id'], name, geburtsdatum, allergien))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('patient_form.html')

@app.route('/patient/<int:id>')
@login_required
def patient_detail(id):
    conn = get_connection()
    patient = conn.execute('SELECT * FROM patienten WHERE id = ? AND nutzer_id = ?',
                           (id, session['nutzer_id'])).fetchone()
    if not patient:
        return redirect(url_for('index'))
    medikamente = conn.execute('SELECT * FROM medikamente WHERE patient_id = ?', (id,)).fetchall()
    conn.close()
    return render_template('patient_detail.html', patient=patient, medikamente=medikamente)

@app.route('/patient/<int:id>/medikament/neu', methods=['GET', 'POST'])
@login_required
def medikament_neu(id):
    if request.method == 'POST':
        name = request.form['name']
        dosierung = request.form['dosierung']
        uhrzeit = request.form['uhrzeit']
        indikation = request.form['indikation']
        conn = get_connection()
        conn.execute('INSERT INTO medikamente (patient_id, name, dosierung, uhrzeit, indikation) VALUES (?, ?, ?, ?, ?)',
                     (id, name, dosierung, uhrzeit, indikation))
        conn.commit()
        conn.close()
        return redirect(url_for('patient_detail', id=id))
    return render_template('medikament_form.html', id=id)

@app.route('/patient/<int:id>/loeschen', methods=['POST'])
@login_required
def patient_loeschen(id):
    conn = get_connection()
    conn.execute('DELETE FROM medikamente WHERE patient_id = ?', (id,))
    conn.execute('DELETE FROM patienten WHERE id = ? AND nutzer_id = ?', (id, session['nutzer_id']))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/patient/<int:id>/qr')
@login_required
def patient_qr(id):
    conn = get_connection()
    patient = conn.execute('SELECT * FROM patienten WHERE id = ? AND nutzer_id = ?',
                           (id, session['nutzer_id'])).fetchone()
    conn.close()
    url = url_for('patient_detail', id=id, _external=True)
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return render_template('qr.html', patient=patient, img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)