from flask import Flask, render_template
import mysql.connector

app=Flask(__name__)

def get_db_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ticket_system",
        port=3307
    )
    return connection

@app.route('/')
def index():
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets")
    tickets_found=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html',tickets=tickets_found)

if __name__=='__main__':
    app.run(debug=True)



