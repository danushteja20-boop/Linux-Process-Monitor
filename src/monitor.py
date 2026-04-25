import psutil
import time
import os

def display_stats():
    # Clear terminal for that "real-time" app feel
    os.system('clear') 
    
    print("="*30)
    print("   ADVANCED PROCESS MONITOR")
    print("="*30)
    
    # CPU & RAM
    print(f"CPU Load:    {psutil.cpu_percent()}%")
    print(f"RAM Usage:   {psutil.virtual_memory().percent}%")
    print("-" * 30)

    # Top 5 Processes by CPU usage
    print(f"{'PID':<8} {'NAME':<20} {'CPU%'}")
    
    # Get processes and sort them
    procs = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            procs.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    # Sort by CPU and show top 5
    top_procs = sorted(procs, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    
    for p in top_procs:
        print(f"{p['pid']:<8} {p['name'][:20]:<20} {p['cpu_percent']}%")

if __name__ == "__main__":
    try:
        while True:
            display_stats()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")
