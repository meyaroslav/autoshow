from src.database.connection import get_connection

def get_models_for_brand(brand_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM brands WHERE name = %s", (brand_name,))
    brand_id = cur.fetchone()[0]

    cur.execute("SELECT name FROM models WHERE brand_id = %s", (brand_id,))
    models = [row[0] for row in cur.fetchall()]

    conn.close()
    return models

def update_car(vin, brand, model, color, transmission, year, mileage, price):
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

    cur.execute("""
        UPDATE cars
        SET brand_id = %s, model_id = %s, color_id = %s, transmission_id = %s,
            year = %s, mileage = %s, price = %s
        WHERE vin = %s
    """, (brand_id, model_id, color_id, transmission_id, year, mileage, price, vin))

    conn.commit()
    cur.close()
    conn.close()