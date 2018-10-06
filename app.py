import os
import sys
import hashlib
import mysql.connector

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="chicken77",
  database="hackathon"
)

email = ""

myCursor = mydb.cursor(prepared=True)

app = Flask(__name__)



@app.route("/", methods=['GET'])
def index():
    return render_template("index5.html")

@app.route("/", methods=['POST'])
def serve_form():
    email = request.form.get("email")
    myCursor.execute("UPDATE tempemail set Email = %s", (email,))
    mydb.commit()


    #these inputs are sanitized
    myCursor.execute("SELECT COUNT(*) FROM Person WHERE Email = %s", (email,))
    myresult = myCursor.fetchall()

    if myresult[0][0]:          #account found
        myCursor.execute("SELECT FirstName FROM Person WHERE Email = %s", (email,))
        myresult = myCursor.fetchone()
        first_name = str(myresult[0].decode())
        display_text = "Hi, " + first_name + ". We're glad to have you back!"

        return render_template('password.html', display_text = display_text)
    else:                                           # user doesn't exist
        return render_template('register.html')

@app.route("/pass", methods=['POST'])
def serve_dashboard_existing_user():
    password = request.form.get("password")

    myCursor.execute("SELECT Email FROM tempemail")
    myresult = myCursor.fetchall()
    db_email = str(myresult[0][0].decode())

    myCursor.execute("SELECT Password FROM Person WHERE Email = %s", (db_email,))
    myresult = myCursor.fetchone()
    # print("our info: " + myresult[0].decode())
    # passwordHash = hashlib.md5(str(myresult[0].decode()).encode()).hexdigest()

    print("[[_ " + db_email + " <------username")
    print(myresult[0].decode() + " <-------password")
    if hashlib.md5(password.encode()).hexdigest() == myresult[0].decode():
        return render_template('dashboard.html')
    else:
        display_text = "Incorrect credentials!"
        return render_template('password.html', display_text = display_text)


@app.route("/dashboard", methods=['POST'])
def serve_dashboard_new_user():
    password = request.form.get("password")
    password2 = request.form.get("password_verify")
    print(password)
    if 8 < len(password) < 15 and password == password2:
        print("passwords are same")
        return render_template("dashboard.html")
    else:
        return render_template("register.html", invalid_password = "Passwords must match and be between 8 and 15 characters.")
