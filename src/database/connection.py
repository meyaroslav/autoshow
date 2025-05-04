import psycopg2

def db_connection():
    return psycopg2.connect(
        dbname="autoshow",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )