from src.database.connection import get_connection

from src.database.connection import get_connection

def get_all_brands():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM brands")
    brands = [row[0] for row in cur.fetchall()]

    conn.close()
    return brands

def get_all_models():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM models")
    models = [row[0] for row in cur.fetchall()]

    conn.close()
    return models

def get_all_colors():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM colors")
    colors = [row[0] for row in cur.fetchall()]

    conn.close()
    return colors

def get_all_transmissions():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM transmissions")
    transmissions = [row[0] for row in cur.fetchall()]

    conn.close()
    return transmissions

def add_car(vin, brand, model, color, transmission, year, mileage, price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM brands WHERE name = %s", (brand,))
    brand_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM models WHERE name = %s", (model,))
    model_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM colors WHERE name = %s", (color,))
    color_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM transmissions WHERE name = %s", (transmission,))
    transmission_id = cur.fetchone()[0]

    status_id = 1

    cur.execute("SELECT COUNT(*) FROM cars WHERE vin = %s", (vin,))
    if cur.fetchone()[0] > 0:
        conn.close()
        raise ValueError("Автомобиль с таким VIN уже существует")

    cur.execute("""
            INSERT INTO cars (vin, brand_id, model_id, color_id, transmission_id, year, mileage, price, status_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (vin, brand_id, model_id, color_id, transmission_id, year, mileage, price, status_id))

    conn.commit()
    cur.close()
    conn.close()