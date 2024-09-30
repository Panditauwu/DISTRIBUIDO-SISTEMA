from monitor import get_system_metrics

def adjust_parameters():
    """
    Ajusta los parámetros del sistema basándose en el uso de CPU y memoria.
    """
    metrics = get_system_metrics()
    
    # Ajusta los parámetros según el uso de CPU
    cpu_usage = metrics['cpu_usage']
    
    if cpu_usage > 80:
        print("Alta carga de CPU. Redistribuir tareas o reducir la carga.")
    elif cpu_usage < 20:
        print("Baja carga de CPU. Se pueden aumentar las tareas en este nodo.")
    else:
        print("Carga de CPU óptima. No se requieren cambios.")
        
if __name__ == "__main__":
    adjust_parameters()
