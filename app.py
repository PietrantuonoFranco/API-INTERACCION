from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    { "email": "admin@example.com", "password": "12345678" },
    { "email": "normie@example.com", "password": "12345678" },
    { "email": "nutri@example.com", "password": "12345678" }
]

kinesiologos = [
    { "nombre": "Dr. Smith", "disponible": True },
    { "nombre": "Dr. Johnson", "disponible": False },
    { "nombre": "Dr. Williams", "disponible": True },
    { "nombre": "Dr. Brown", "disponible": False }
]

##PARA VERIFICAR SI CORRE!
@app.route('/')
def index():
    return jsonify({"status": "ok"})


##DESCUENTOS
@app.route('/verificarUsuario', methods=['POST'])
def verificarUsuario():
    data = request.json
    for i in usuarios:
        if i["email"] == data["email"] and i["password"] == data["password"]:
            return jsonify({"status": "Exitoso","descuento": "0.3"})
        
@app.route('/obtenerDescuento', methods=['GET'])
def obtenerDescuento():
    return jsonify({"descuento": "0.3"})


##KINESIOILOGOS
@app.route('/agendarConsulta', methods=['POST'])
def agendarConsulta():
    data = request.json
    fecha = data.get("fecha")
    kinesiologo = data.get("kinesiologo")
    tema_consulta = data.get("tema_consulta")
    descripcion = data.get("descripcion")
    
    if not all([fecha, kinesiologo, tema_consulta, descripcion]):
        return jsonify({"status": "error", "message": "Faltan datos"}), 400
    
    # Verificar disponibilidad del kinesiologo
    for k in kinesiologos:
        if k["nombre"] == kinesiologo:
            if not k["disponible"]:
                return jsonify({"status": "error", "message": "Kinesiologo no disponible"}), 400
            break
    else:
        return jsonify({"status": "error", "message": "Kinesiologo no encontrado"}), 400
    
    # Aquí podrías agregar la lógica para guardar la consulta en una base de datos o similar
    return jsonify({"status": "ok", "message": "Consulta agendada correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)