import os
import sys
import hashlib

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# engine = create_engine('')
# db = scoped_session(sessionmaker(bind=engine))

correct_email = 'test_email'
correct_password = hashlib.md5('testpass'.encode()).hexdigest()

email = None

@app.route("/", methods=['GET'])
def index():
    return render_template("index5.html")

@app.route("/", methods=['POST'])
def serve_form():
    email = request.form.get("email")
    #these inputs are sanitized
    #check = db.execute("SELECT * FROM users WHERE email == :email", {"email": email}).fetchone()
    if email == correct_email:
        first_name = "Trevor"
        display_text = "Hi, " + first_name + ". We're glad to have you back!"
        return render_template('password.html', display_text = display_text)
    else:                                           # user doesn't exist
        return render_template('register.html')

@app.route("/#pass", methods=['POST'])
def serve_dashboard_existing_user():
    password = request.form.get("password")
    #TODO make sure password is correct from database
    if hashlib.md5(password.encode()).hexdigest() == correct_password: #select password where email = email, compare to correct_password
        return render_template('dashboard.html')
    else:
        display_text = "Incorrect credentials!"
        return render_template('password.html', display_text = display_text)


@app.route("/dashboard", methods=['POST'])
def serve_dashboard_new_user():
    # TODO validate password (length, characters, etc). Also, hash

    return render_template("dashboard.html")
