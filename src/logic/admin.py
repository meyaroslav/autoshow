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

def get_car_by_vin(vin):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT cars.vin, brands.name, models.name, colors.name,
               transmissions.name, cars.year, cars.mileage, cars.price, status.name
        FROM cars
        JOIN brands ON cars.brand_id = brands.id
        JOIN models ON cars.model_id = models.id
        JOIN colors ON cars.color_id = colors.id
        JOIN transmissions ON cars.transmission_id = transmissions.id
        JOIN status ON cars.status_id = status.id
        WHERE cars.vin = %s
    """, (vin,))

    car_data = cur.fetchone()
    conn.close()

    if car_data:
        return car_data
    else:
        raise ValueError("Автомобиль с таким VIN не найден")

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

def get_all_filters():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM brands")
    brands = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT name FROM models")
    models = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT name FROM colors")
    colors = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT name FROM transmissions")
    transmissions = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT name FROM status")
    status = [row[0] for row in cur.fetchall()]

    conn.close()

    return {
        "brands": brands,
        "models": models,
        "colors": colors,
        "transmissions": transmissions,
        "status": status,
    }

def filter_cars(filters: dict):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT cars.vin, brands.name, models.name, colors.name,
           transmissions.name, cars.year, cars.mileage, cars.price, status.name
    FROM cars
    JOIN brands ON cars.brand_id = brands.id
    JOIN models ON cars.model_id = models.id
    JOIN colors ON cars.color_id = colors.id
    JOIN transmissions ON cars.transmission_id = transmissions.id
    JOIN status ON cars.status_id = status.id
    WHERE 1=1
    """
    params = []

    if filters["brand"]:
        query += " AND brands.name = %s"
        params.append(filters["brand"])
    if filters["model"]:
        query += " AND models.name = %s"
        params.append(filters["model"])
    if filters["color"]:
        query += " AND colors.name = %s"
        params.append(filters["color"])
    if filters["transmission"]:
        query += " AND transmissions.name = %s"
        params.append(filters["transmission"])
    if filters["status"]:
        query += " AND status.name = %s"
        params.append(filters["status"])
    if filters["mileage_min"] is not None:
        query += " AND cars.mileage >= %s"
        params.append(filters["mileage_min"])
    if filters["mileage_max"] is not None:
        query += " AND cars.mileage <= %s"
        params.append(filters["mileage_max"])
    if filters["year_min"] is not None:
        query += " AND cars.year >= %s"
        params.append(filters["year_min"])
    if filters["year_max"] is not None:
        query += " AND cars.year <= %s"
        params.append(filters["year_max"])

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    conn.close()

    col_names = [
        "VIN", "Марка", "Модель", "Цвет", "Тип трансмиссии",
        "Год выпуска", "Пробег", "Цена", "Статус"
    ]
    return rows, col_names