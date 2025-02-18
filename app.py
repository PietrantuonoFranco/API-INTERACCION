from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa la extensión CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

usuarios = [
    { "email": "admin@example.com", "password": "12345678" },
    { "email": "normie@example.com", "password": "12345678" },
    { "email": "nutri@example.com", "password": "12345678" }
]

kinesiologos = [
    { "id": 1, "nombre": "Dra. Smith", "disponible": True, "especialidad" : "Traumatología" },
    { "id": 2,"nombre": "Dr. Johnson", "disponible": False, "especialidad" : "Deportólogo"},
    { "id": 3,"nombre": "Dr. Williams", "disponible": True, "especialidad" : "Ergonometría"},
    { "id": 4,"nombre": "Dr. Brown", "disponible": False, "especialidad" : "Geriatría"}
]

## PARA VERIFICAR SI CORRE!
@app.route('/')
def index():
    return jsonify({"status": "ok"})

## DESCUENTOS
@app.route('/verificarUsuario', methods=['POST'])
def verificarUsuario():
    data = request.json
    for i in usuarios:
        if i["email"] == data["email"] and i["password"] == data["password"]:
            return jsonify({"status": "ok", "Descuento": "0.3"})
    return jsonify({"status": "error", "message": "Credenciales incorrectas"}), 401

## KINESIOLOGOS
@app.route('/agendar-consulta', methods=['POST'])
def agendarConsulta():
    data = request.json
    fecha = data.get("fecha")
    horario = data.get("horario")
    doctor = data.get("doctor")
    tema_consulta = data.get("tipoConsulta")
    descripcion = data.get("descripcion")
    paciente = data.get("paciente")
    
    if not all([fecha, horario, doctor, tema_consulta, descripcion, paciente]):
        return jsonify({"status": "error", "message": "Faltan datos"}), 400
    
    else:
        return jsonify({"status": "ok", "message": "Consulta agendada correctamente", "dia": fecha, "horario": horario, "doctor" : doctor, "paciente" : paciente}), 200

@app.route('/obtener-kinesiologos', methods=['GET'])
def getKinesiologos():
    return jsonify({
        "status": "ok", 
        "message": "Kinesiologos obtenidos exitosamente.",
        "kinesiologos": kinesiologos
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)