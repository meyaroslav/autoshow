from src.database.connection import get_connection

def cars_data():
    conn = get_connection()
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
    conn = get_connection()
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
    conn = get_connection()
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
    conn = get_connection()
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

def delete_car_by_vin(vin):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM cars WHERE vin = %s", (vin,))
    conn.commit()

    cur.close()
    conn.close()