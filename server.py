from flask import Flask, jsonify
from flask_cors import CORS


#  el servidor Flask define una ruta /data que devuelve un JSON con un mensaje simple. Se habilita CORS para toda la aplicación mediante CORS(app)

app = Flask(__name__)
#CORS(app)  # Habilitar CORS para toda la aplicación
# CORS(app, resources={r"/data": {"origins": "http://localhost:80"}})

@app.route('/data')
def get_data():
    data = {'message': '¡Hola desde el servidor!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
