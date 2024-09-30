from monitor import get_system_metrics

def redistribute_load(nodes):
    """
    Redistribuye la carga de trabajo entre los nodos dependiendo de sus recursos.
    """
    for node in nodes:
        metrics = get_system_metrics()
        if metrics['cpu_usage'] > 80:
            print(f"El nodo {node} tiene una carga alta. Redistribuyendo tareas...")
            # Implementa aquí la lógica para mover tareas a otros nodos con menos carga
        else:
            print(f"El nodo {node} está bajo una carga aceptable.")
            
if __name__ == "__main__":
    # Ejemplo con una lista de nodos
    nodes = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002"]
    redistribute_load(nodes)
