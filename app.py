from flask import Flask, render_template , request , redirect , url_for
import secrets
import string
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)


def generate_short_code(length=5):
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return ''.join(secrets.choice(characters) for _ in range(length))

def create_table(rooom_id):
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
        cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT)".format(rooom_id))
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())
        cursor.execute("SELECT * FROM {}".format(rooom_id))
        print(cursor.fetchall())
    finally:
        connection.close()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<room_id>')
def room(room_id):
    return render_template('room.html', room_id=room_id)

@app.route('/create_room')
def create_room():
    room_id = generate_short_code()
    create_table(room_id)
    #return render_template('room.html', room_id=room_id)
    return redirect(url_for('room', room_id=room_id))

if __name__ == '__main__':
    app.run(debug=True)