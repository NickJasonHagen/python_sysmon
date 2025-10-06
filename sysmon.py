# requires dep: pip install psutil
import psutil
print("CPU usage (%):", psutil.cpu_percent(interval=0.5))
ram = psutil.virtual_memory()
print("RAM usage (%):", ram.percent)
print("RAM used (GB):", round(ram.used / 1e9, 2))
