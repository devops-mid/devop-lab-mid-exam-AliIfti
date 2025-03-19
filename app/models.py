from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))  # Optional field
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(10))  # New phone field
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def validate_phone(phone):
    return re.match(r"^\d{10}$", phone)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    if not validate_phone(data["phone"]):
        return jsonify({"error": "Invalid phone number"}), 400
    # Save to database
    return jsonify({"message": "Success"})
