# App Routes

from flask import Flask, render_template, request, redirect, url_for
from .models import *
from flask import current_app as app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        uname = request.form.get("user_name")
        pwd = request.form.get("password")
        usr = User_Info.query.filter_by(email=uname, password=pwd).first()
        
        if usr and usr.role == 0:  # Existed and Admin
            return redirect(url_for("admin_dashboard"))
        elif usr and usr.role == 1:  # Existed and User
            return redirect(url_for("user_dashboard"))
        else: 
            return render_template("login.html", msg= "Invalid User Credentials...")
        
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        uname = request.form.get("user_name")
        pwd = request.form.get("password")
        full_name = request.form.get("full_name")
        address = request.form.get("location")
        pin = request.form.get("pin_code")
        
        # Check if user already exists
        existing_user = User_Info.query.filter_by(email=uname).first()
        if existing_user:
            return render_template("signup.html", error=" Sorry, Email already registered")
        
        # Register new user
        new_usr = User_Info(email=uname, password=pwd, full_name=full_name, address=address, pincode=pin, role=1)
        db.session.add(new_usr)
        db.session.commit()
        return render_template("login.html", msg = "Registration is successful, Try login now please")  # Redirect to login page after registration
    
    return render_template("signup.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/user_dashboard")
def user_dashboard():
    return render_template("user_dashboard.html")