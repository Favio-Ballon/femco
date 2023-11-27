import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="femcoprueba",
    user="postgres",
    password="root"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

def cursor():
    return cur
def connection():
    return conn
