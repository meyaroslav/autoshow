from src.database.connection import db_connection

def cars_data():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            cars.vin AS "VIN",
            brands.name AS "Марка",
            models.name AS "Модель",
            colors.name AS "Цвет",
            transmissions.name AS "Тип трансмиссии",
            cars.year AS "Год выпуска",
            cars.mileage AS "Пробег",
            cars.price AS "Цена",
            status.name AS "Статус"
        FROM cars
        JOIN brands ON cars.brand_id = brands.id
        JOIN models ON cars.model_id = models.id
        JOIN colors ON cars.color_id = colors.id
        JOIN transmissions ON cars.transmission_id = transmissions.id
        JOIN status ON cars.status_id = status.id;
    """)
    res = cur.fetchall()
    col = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return res, col

def clients_data():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            full_name AS "ФИО",
            phone AS "Телефон",
            email AS "Почта"
        FROM clients
    """)
    res = cur.fetchall()
    col = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return res, col

def sales_data():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            cars.vin AS "VIN автомобиля",
            clients.full_name AS "Клиент",
            sales.date AS "Дата продажи",
            sales.price AS "Цена"
        FROM sales
        JOIN cars ON sales.car_id = cars.id
        JOIN clients ON sales.client_id = clients.id;
    """)
    res = cur.fetchall()
    col = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return res, col

def users_data():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            login AS "Логин",
            password AS "Пароль",
            role AS "Роль"
        FROM users;
    """)
    res = cur.fetchall()
    col = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return res, col

def get_brands():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM brands")
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res

def get_models():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM models")
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res

def get_colors():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM colors")
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res

def get_transmissions():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM transmissions")
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res

def get_statuses():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM status")
    res = cur.fetchall()

    cur.close()
    conn.close()

    return res

def insert_car(vin, brand_id, model_id, color_id, transmission_id, year, mileage, price):
    conn = db_connection()
    cur = conn.cursor()

    status_id = 1
    cur.execute("""
        INSERT INTO cars (vin, brand_id, model_id, color_id, transmission_id, year, mileage, price, status_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (vin, brand_id, model_id, color_id, transmission_id, year, mileage, price, status_id))

    conn.commit()
    cur.close()
    conn.close()
