import os
import sys

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgres://olxpdkjidxzijo:6c0ff6d277bd117d6e615144dab8b3fe26e190e0788c30c9aa4c6de74076af2d@ec2-54-235-242-63.compute-1.amazonaws.com:5432/d25m2jqruo7e1o')
db = scoped_session(sessionmaker(bind=engine))

email = None

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def serve_form():
    email = request.form.get("Username")
    #these inputs are sanitized
    check = db.execute("SELECT * FROM users WHERE email == :email", {"email": email}).fetchone()
    if not check == None:                           # user exists
        return render_template('password.html')
    else:                                           # user doesn't exist
        return render_template('register.html')

@app.route("/", methods=['POST'])
def serve_dashboardteam-9_existing_user():
    password = request.form.get("Password")
    #TODO validate password (length, characters, etc). Also, hash
    #TODO make sure password is correct from database

    return render_template('dashboard.html')

@app.route("/", methods=['POST'])
def serve_dashboard_new_user():
