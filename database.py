import sqlite3

def get_connection():#Verbindung zur Datenbank
    conn = sqlite3.connect('mediplan.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db(): # ertsellt zwei Tabellen - Patienten, Medikamente
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS patienten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            geburtsdatum TEXT NOT NULL,
            allergien TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS medikamente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            dosierung TEXT NOT NULL,
            uhrzeit TEXT NOT NULL,
            indikation TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patienten(id)
        )
    ''')
    conn.commit()
    conn.close()