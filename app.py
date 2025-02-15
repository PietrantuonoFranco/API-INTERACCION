from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    { "email": "admin@example.com", "password": "12345678" },
    { "email": "normie@example.com", "password": "12345678" },
    { "email": "nutri@example.com", "password": "12345678" }
]

@app.route('/')
def index():
    return jsonify({"status": "ok"})

@app.route('/verificarUsuario', methods=['POST'])
def verificarUsuario():
    data = request.json
    for i in usuarios:
        if i["email"] == data["email"] and i["password"] == data["password"]:
            return jsonify({"status": "ok","Descuento": "0.3"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)