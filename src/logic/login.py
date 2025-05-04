from src.database.connection import get_connection

def auth(login: str, password: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT role FROM users WHERE login = %s AND password = %s", (login, password))
    res = cur.fetchone()

    cur.close()
    conn.close()

    if res:
        return True, res[0]
    return False, ""