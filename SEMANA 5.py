from flask import Flask, jsonify
from monitor import get_system_metrics

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    """
    Retorna el estado y las métricas del nodo.
    """
    return jsonify({"status": "ok", "metrics": get_system_metrics()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Cambia el puerto para crear múltiples nodos
