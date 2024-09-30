import requests

def check_node_status(node_url):
    """
    Verifica el estado de un nodo en el sistema distribuido.
    """
    try:
        response = requests.get(f"{node_url}/status")
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False

def recover_node(node_url):
    """
    Realiza la recuperación de un nodo que ha fallado.
    """
    if not check_node_status(node_url):
        print(f"El nodo {node_url} ha fallado. Iniciando proceso de recuperación...")
        # Aquí podrías agregar lógica para reiniciar el nodo o reasignar tareas.
        # Por ejemplo, llamar a otro nodo para tomar las tareas del nodo caído.
    else:
        print(f"El nodo {node_url} está funcionando correctamente.")
        
if __name__ == "__main__":
    recover_node("http://localhost:5500")
