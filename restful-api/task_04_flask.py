#!/usr/bin/python3
"""Module that implements a simple API using Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Returns welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Returns list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Returns OK"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns user data for given username"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary"""
    try:
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        if 'username' not in data:
            return jsonify({"error": "Username is required"}), 400
        if data['username'] in users:
            return jsonify({"error": "Username already exists"}), 409
        users[data['username']] = data
        return jsonify({"message": "User added", "user": data}), 201
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
