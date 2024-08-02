import psutil
import platform
from datetime import datetime

def log_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = (f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory.percent}% | "
                 f"Disk: {disk.percent}%\n")

    with open("system_metrics.log", "a") as log_file:
        log_file.write(log_entry)

if platform.system() == "Windows":
    log_system_metrics()
