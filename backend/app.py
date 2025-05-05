from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "API online"}

# Cargar los usuarios desde el archivo externo
with open("users.json", "r") as f:
    USERS = json.load(f)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    for user in USERS:
        if user["email"] == email and user["password"] == password:
            return jsonify({ "url": user["url"] })

    return jsonify({ "error": "Credenciales incorrectas" }), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
