from src.database.connection import get_connection

def update_client(client_id, full_name, phone, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM clients WHERE (phone = %s OR email = %s) AND id != %s", (phone, email, client_id))
    if cur.fetchone()[0] > 0:
        raise ValueError("Клиент с таким телефоном или почтой уже существует")

    cur.execute("UPDATE clients SET full_name = %s, phone = %s, email = %s WHERE id = %s", (full_name, phone, email, client_id))

    conn.commit()
    cur.close()
    conn.close()
