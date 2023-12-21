from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'kingcobraismysecretkey'

db = mysql.connector.connect(
host = "localhost",
user = "your username",
password = "yourpassword",
database = "KINGDATA"


)
cursor = db.cursor()

@app.route('/register'  , methods = [ 'GET' , 'POST'])
def register():
    # Your code for the register route goes here
    if request.method == 'POST'    :
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users(username , password) VALUES (%s,%s)"  , (username,password))
        db.commit()
        return redirect(url_for('login'))
        return render_template('register.html')

@app.route('/login'  , methods = [ 'GET' , 'POST'])
def login():
    if request.method == 'POST'    :
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s" ,(username, password)) 
        user = cursor.fetchone()
        if user:
            session['user_id']=user[0] 

        



    
    

@app.route('/todo' , methods = [ 'GET' ,'POST'])
def todo_list():


    ...

@app.route('/logout')
def logout():

    ...


