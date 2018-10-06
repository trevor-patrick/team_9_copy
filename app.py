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

myCursor = mydb.cursor(prepared=True)           #Using prepared statements to prevent SQL injection

app = Flask(__name__)                           #Server microfamework



@app.route("/", methods=['GET'])            
def index():                                    #Home page
    return render_template("index5.html")

@app.route("/", methods=['POST'])
def serve_form():                               #Decide weather user is new or existing. Then, serve appropriate page
    email = request.form.get("email")
    myCursor.execute("UPDATE tempemail set Email = %s", (email,))
    mydb.commit()


    #these inputs are sanitized
    myCursor.execute("SELECT COUNT(*) FROM Person WHERE Email = %s", (email,))
    myresult = myCursor.fetchall()

    if myresult[0][0]:      #account found: user already exists. we will greet and provide password input field
        myCursor.execute("SELECT FirstName FROM Person WHERE Email = %s", (email,))
        myresult = myCursor.fetchone()
        first_name = str(myresult[0].decode())
        display_text = "Hi, " + first_name.title() + ". We're glad to have you back!"

        return render_template('password.html', display_text = display_text)
    else:                   # user doesn't exist. we will provide oppertunity to sign up
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
        return render_template('financial.html')
    else:
        display_text = "Incorrect credentials!"
        return render_template('password.html', display_text = display_text)


@app.route("/dashboard", methods=['POST'])
def serve_dashboard_new_user():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    phonenumber = request.form.get("phonenumber")
    zipcode = request.form.get("zipcode")
    password = request.form.get("password")
    password2 = request.form.get("password_verify")
    passwordhash = hashlib.md5(password.encode()).hexdigest()
    print(password)
    if 8 < len(password) < 15 and password == password2:

        myCursor.execute("SELECT Email From tempemail;")
        emailResult = myCursor.fetchone()
        print("Email Result: -----------> " + emailResult[0].decode())
        print("{} {} {} {} {} {}".format(firstname,lastname,phonenumber,zipcode,password,password2))
        myCursor.execute("INSERT INTO person (FirstName, LastName, Email, Password, ZipCode, PhoneNumber) VALUES('%s', '%s', '%s', '%s', '%d', '%d');" % (firstname, lastname, emailResult[0].decode(), passwordhash, int(zipcode), int(phonenumber)))
        mydb.commit()

        return render_template("financial.html")
    else:
        return render_template("register.html", invalid_password = "Passwords must match and be between 8 and 15 characters.")

@app.route("/budget", methods=['POST'])
def serve_financials():
    goal = request.form.get("goal")
    gains = request.form.get("gains")
    losses = request.form.get("losses")
    return render_template("financial.html", goal_var = 100)

@app.route("/index5", methods=['GET'])
def serve_index5():
    return render_template('index5.html')

@app.route("/index6", methods=['GET'])
def serve_index6():
    return render_template('index6.html')

@app.route("/index7", methods=['GET'])
def serve_index7():
    return render_template('index7.html')