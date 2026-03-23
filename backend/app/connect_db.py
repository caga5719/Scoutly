import psycong2

conn = psycong2.connect("dbname=test user=postgres")

cur = conn.cursor()

cur.execute("CREATE TABLE sales_user")