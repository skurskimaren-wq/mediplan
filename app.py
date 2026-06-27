from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, init_db
import qrcode
import io
import base64

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/')
def index():
    conn = get_connection()
    patienten = conn.execute('SELECT * FROM patienten').fetchall()
    conn.close()
    return render_template('index.html', patienten=patienten)

@app.route('/patient/neu', methods=['GET', 'POST'])
def patient_neu():
    if request.method == 'POST':
        name = request.form['name']
        geburtsdatum = request.form['geburtsdatum']
        allergien = request.form['allergien']
        conn = get_connection()
        conn.execute('INSERT INTO patienten (name, geburtsdatum, allergien) VALUES (?, ?, ?)',
                     (name, geburtsdatum, allergien))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('patient_form.html')

@app.route('/patient/<int:id>')
def patient_detail(id):
    conn = get_connection()
    patient = conn.execute('SELECT * FROM patienten WHERE id = ?', (id,)).fetchone()
    medikamente = conn.execute('SELECT * FROM medikamente WHERE patient_id = ?', (id,)).fetchall()
    conn.close()
    return render_template('patient_detail.html', patient=patient, medikamente=medikamente)

@app.route('/patient/<int:id>/medikament/neu', methods=['GET', 'POST'])
def medikament_neu(id):
    if request.method == 'POST':
        name = request.form['name']
        dosierung = request.form['dosierung']
        uhrzeit = request.form['uhrzeit']
        indikation = request.form['indikation']
        conn = get_connection()
        conn.execute(
            'INSERT INTO medikamente (patient_id, name, dosierung, uhrzeit, indikation) VALUES (?, ?, ?, ?, ?)',
            (id, name, dosierung, uhrzeit, indikation))
        conn.commit()
        conn.close()
        return redirect(url_for('patient_detail', id=id))
    return render_template('medikament_form.html', id=id)

@app.route('/patient/<int:id>/qr')
def patient_qr(id):
    conn = get_connection()
    patient = conn.execute('SELECT * FROM patienten WHERE id = ?', (id,)).fetchone()
    conn.close()
    url = url_for('patient_detail', id=id, _external=True)
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return render_template('qr.html', patient=patient, img_base64=img_base64)

if __name__ == '__main__':
    @app.route('/patient/<int:id>/loeschen', methods=['POST'])
    def patient_loeschen(id):
        conn = get_connection()
        conn.execute('DELETE FROM medikamente WHERE patient_id = ?', (id,))
        conn.execute('DELETE FROM patienten WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    app.run(debug=True)