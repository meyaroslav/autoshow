from src.database.connection import get_connection

def add_client(full_name, phone, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM clients WHERE phone = %s OR email = %s", (phone, email))
    if cur.fetchone()[0] > 0:
        raise ValueError("Клиент с таким телефоном или почтой уже существует")

    cur.execute("INSERT INTO clients (full_name, phone, email) VALUES (%s, %s, %s)", (full_name, phone, email))

    conn.commit()
    cur.close()
    conn.close()