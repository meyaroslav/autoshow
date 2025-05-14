from src.database.connection import get_connection

def get_clients():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT full_name FROM clients")
    clients = cur.fetchall()

    conn.close()
    return clients

def get_available_cars():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT CONCAT(brands.name, ' ', models.name, ' ', colors.name) AS car_info, cars.vin
        FROM cars
        JOIN brands ON cars.brand_id = brands.id
        JOIN models ON cars.model_id = models.id
        JOIN colors ON cars.color_id = colors.id
        WHERE cars.status_id = 1  -- Статус "В наличии"
    """)
    cars = cur.fetchall()

    conn.close()
    return cars

def get_car_price(vin):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT price FROM cars WHERE vin = %s", (vin,))
    price = cur.fetchone()

    conn.close()

    if price:
        return price[0]
    else:
        raise ValueError("Цена автомобиля не найдена")

def add_sale(client_name, car_vin, sale_date, price):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM clients WHERE full_name = %s", (client_name,))
    client_id = cur.fetchone()[0]

    cur.execute("SELECT id FROM cars WHERE vin = %s", (car_vin,))
    car_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO sales (car_id, client_id, date, price)
        VALUES (%s, %s, %s, %s)
    """, (car_id, client_id, sale_date, price))

    cur.execute("UPDATE cars SET status_id = 2 WHERE vin = %s", (car_vin,))

    conn.commit()
    cur.close()
    conn.close()
