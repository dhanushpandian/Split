import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

timeout = int(os.getenv("DB_TIMEOUT"))
connection = pymysql.connect(
    charset=os.getenv("DB_CHARSET"),
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    read_timeout=timeout,
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")
    print(cursor.fetchall())
    cursor.execute("sHOW TABLES")
    tables=cursor.fetchall()
    print(tables)
    for i in tables:
        print("deleting table",i['Tables_in_defaultdb'])
        cursor.execute("DROP TABLE {}".format(i['Tables_in_defaultdb']))
finally:
    connection.close()
