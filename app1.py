# from flask import Flask, render_template , request , redirect , url_for
# import secrets
# import string
# import pymysql
# import os
# from dotenv import load_dotenv

# load_dotenv()
# app=Flask(__name__)


# def generate_short_code(length=5):
#     characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
#     return ''.join(secrets.choice(characters) for _ in range(length))

# # def create_table(rooom_id):
# #     timeout = int(os.getenv("DB_TIMEOUT"))
# #     connection = pymysql.connect(
# #         charset=os.getenv("DB_CHARSET"),
# #         connect_timeout=timeout,
# #         cursorclass=pymysql.cursors.DictCursor,
# #         db=os.getenv("DB_NAME"),
# #         host=os.getenv("DB_HOST"),
# #         password=os.getenv("DB_PASSWORD"),
# #         read_timeout=timeout,
# #         port=int(os.getenv("DB_PORT")),
# #         user=os.getenv("DB_USER"),
# #         write_timeout=timeout,
# #     )

# #     try:
# #         cursor = connection.cursor()
# #         cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT)".format(rooom_id))
# #         cursor.execute("SHOW TABLES")
# #         print(cursor.fetchall())
# #         cursor.execute("SELECT * FROM {}".format(rooom_id))
# #         print(cursor.fetchall())
# #     finally:
# #         connection.close()

# def create_table(room_id):
#     timeout = int(os.getenv("DB_TIMEOUT"))
#     connection = pymysql.connect(
#         charset=os.getenv("DB_CHARSET"),
#         connect_timeout=timeout,
#         cursorclass=pymysql.cursors.DictCursor,
#         db=os.getenv("DB_NAME"),
#         host=os.getenv("DB_HOST"),
#         password=os.getenv("DB_PASSWORD"),
#         read_timeout=timeout,
#         port=int(os.getenv("DB_PORT")),
#         user=os.getenv("DB_USER"),
#         write_timeout=timeout,
#     )

#     try:
#         cursor = connection.cursor()
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {room_id}_expenses (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 description TEXT,
#                 amount DECIMAL(10, 2),
#                 paid_by INT,
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {room_id}_users (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255),
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {room_id}_participants (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 expense_id INT,
#                 user_id INT,
#                 amount DECIMAL(10, 2),
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
#         connection.commit()
#     finally:
#         connection.close()


# @app.route('/')
# def index():
#     return render_template('index.html')

# # @app.route('/<room_id>')
# # def room(room_id):
# #     return render_template('room.html', room_id=room_id)

# @app.route('/create_room')
# def create_room():
#     room_id = generate_short_code()
#     create_table(room_id)
#     #return render_template('room.html', room_id=room_id)
#     return redirect(url_for('room', room_id=room_id))

# @app.route('/<room_id>/add_expense', methods=['POST'])
# def add_expense(room_id):
#     description = request.form['description']
#     amount = request.form['amount']
#     paid_by = request.form['paid_by']

#     timeout = int(os.getenv("DB_TIMEOUT"))
#     connection = pymysql.connect(
#         charset=os.getenv("DB_CHARSET"),
#         connect_timeout=timeout,
#         cursorclass=pymysql.cursors.DictCursor,
#         db=os.getenv("DB_NAME"),
#         host=os.getenv("DB_HOST"),
#         password=os.getenv("DB_PASSWORD"),
#         read_timeout=timeout,
#         port=int(os.getenv("DB_PORT")),
#         user=os.getenv("DB_USER"),
#         write_timeout=timeout,
#     )

#     try:
#         cursor = connection.cursor()
#         cursor.execute("""
#             INSERT INTO {} (description, amount, paid_by)
#             VALUES (%s, %s, %s)
#         """.format(room_id), (description, amount, paid_by))
#         connection.commit()
#     finally:
#         connection.close()

#     return redirect(url_for('room', room_id=room_id))

# @app.route('/<room_id>')
# def room(room_id):
#     timeout = int(os.getenv("DB_TIMEOUT"))
#     connection = pymysql.connect(
#         charset=os.getenv("DB_CHARSET"),
#         connect_timeout=timeout,
#         cursorclass=pymysql.cursors.DictCursor,
#         db=os.getenv("DB_NAME"),
#         host=os.getenv("DB_HOST"),
#         password=os.getenv("DB_PASSWORD"),
#         read_timeout=timeout,
#         port=int(os.getenv("DB_PORT")),
#         user=os.getenv("DB_USER"),
#         write_timeout=timeout,
#     )

#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM {}".format(room_id))
#         expenses = cursor.fetchall()
#     finally:
#         connection.close()

#     return render_template('room.html', room_id=room_id, expenses=expenses)


# @app.route('/<room_id>/add_user', methods=['POST'])
# def add_user(room_id):
#     name = request.form['name']
#     timeout = int(os.getenv("DB_TIMEOUT"))
#     connection = pymysql.connect(
#         charset=os.getenv("DB_CHARSET"),
#         connect_timeout=timeout,
#         cursorclass=pymysql.cursors.DictCursor,
#         db=os.getenv("DB_NAME"),
#         host=os.getenv("DB_HOST"),
#         password=os.getenv("DB_PASSWORD"),
#         read_timeout=timeout,
#         port=int(os.getenv("DB_PORT"))
#     )
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import secrets
import string
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def generate_short_code(length=5):
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return ''.join(secrets.choice(characters) for _ in range(length))

def get_db_connection():
    return pymysql.connect(
        db=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        charset=os.getenv("DB_CHARSET"),
        connect_timeout=int(os.getenv("DB_TIMEOUT")),
        read_timeout=int(os.getenv("DB_TIMEOUT")),
        write_timeout=int(os.getenv("DB_TIMEOUT")),
        cursorclass=pymysql.cursors.DictCursor
    )

def create_tables(room_id, connection):
    cursor = connection.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {room_id}_expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT,
            amount DECIMAL(10, 2),
            paid_by INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {room_id}_users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {room_id}_participants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            expense_id INT,
            user_id INT,
            amount DECIMAL(10, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<room_id>')
def room(room_id):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {room_id}_expenses")
        expenses = cursor.fetchall()
        cursor.execute(f"SELECT * FROM {room_id}_users")
        users = cursor.fetchall()
    finally:
        connection.close()

    return render_template('room.html', room_id=room_id, expenses=expenses, users=users)

@app.route('/<room_id>/add_user', methods=['POST'])
def add_user(room_id):
    name = request.form['name']
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {room_id}_users (name) VALUES (%s)", (name,))
        connection.commit()
    finally:
        connection.close()
    return redirect(url_for('room', room_id=room_id))

@app.route('/<room_id>/add_expense', methods=['POST'])
def add_expense(room_id):
    description = request.form['description']
    amount = request.form['amount']
    paid_by = request.form['paid_by']
    participants = request.form.getlist('participants')
    
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO {room_id}_expenses (description, amount, paid_by)
            VALUES (%s, %s, %s)
        """, (description, amount, paid_by))
        expense_id = cursor.lastrowid
        for user_id in participants:
            cursor.execute(f"""
                INSERT INTO {room_id}_participants (expense_id, user_id, amount)
                VALUES (%s, %s, %s)
            """, (expense_id, user_id, amount / len(participants)))
        connection.commit()
    finally:
        connection.close()
    return redirect(url_for('room', room_id=room_id))

@app.route('/create_room')
def create_room():
    room_id = generate_short_code()
    connection = get_db_connection()
    try:
        create_tables(room_id, connection)
    finally:
        connection.close()
    return redirect(url_for('room', room_id=room_id))

if __name__ == '__main__':
    app.run(debug=True)
