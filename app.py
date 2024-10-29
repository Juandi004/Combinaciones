from flask import Flask, request, jsonify
from src import generar_combinaciones  # Importar desde el paquete src

app = Flask(__name__)

@app.route('/combinaciones', methods=['POST'])
def handle_combinaciones():
    data = request.json
    elementos = data.get('elementos', [])
    r = data.get('r', 2)
    
    # Llamar a la función de combinaciones
    combs = generar_combinaciones(elementos, r)
    return jsonify(combs)

if __name__ == '__main__':
    app.run(debug=True)
