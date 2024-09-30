import psutil

def get_system_metrics():
    """
    Recolecta las métricas del sistema como uso de CPU y memoria.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total,
        "memory_available": memory_info.available,
        "memory_used": memory_info.used,
        "memory_percent": memory_info.percent
    }

if __name__ == "__main__":
    # Prueba de monitoreo
    metrics = get_system_metrics()
    print("Métricas del sistema:", metrics)
