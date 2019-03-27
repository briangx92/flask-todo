import psycopg2

conn = psycopg2.connect("dbname=Flask-Todo user=admin password=password host=localhost")

cur = conn.cursor()