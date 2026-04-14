from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app=Flask(__name__)
app.secret_key='capy123'

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
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets")
    tickets_found=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html',tickets=tickets_found, username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        conn=get_db_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user=cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            session['user_id']=user['id']
            session['username']=user['username']
            return redirect(url_for('index'))
        return "Invalid information!"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        conn=get_db_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO users(username,password) VALUES (%s, %s)",(username, password))
            conn.commit()
            return redirect(url_for('login'))
        except:
            return "Username already exists!"
        finally:
            cursor.close()
            conn.close()
    return render_template('signup.html')
        

@app.route('/add', methods=['GET','POST'])
def add_ticket():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        user_id=request.form['user_id']
        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO tickets(title, description, user_id) VALUES (%s, %s, %s)",(title, description, user_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_ticket.html')
        
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)



