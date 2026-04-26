# 🐧 Linux Process Monitor

A lightweight, real-time system resource tracker for Linux. This tool provides a live view of CPU and Memory consumption while identifying and ranking resource-heavy processes.

 # 📷 Demo
![Demo](assets/Linux-Process_Monitor.gif)

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+**
* **Linux OS** (Ubuntu, Fedora, Debian, etc.)

### Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/danushteja20-boop/Linux-Process-Monitor.git](https://github.com/danushteja20-boop/Linux-Process-Monitor.git)
   cd Linux-Process-Monitor

```
 2. **Setup Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
   ```
 3. **Install Dependencies:**
   ```bash
   pip install psutil
   
   ```
 4. **Run the Monitor:**
   ```bash
   python3 src/main.py
   
   ```
## 🔍 Code Explanation
The project is built to handle real-time system diagnostics through efficient data polling:
 * **System Metrics:** Uses psutil.cpu_percent() and psutil.virtual_memory() to pull global hardware stats.
 * **Process Handling:** Iterates through the Linux process tree to capture PID, Name, and Memory usage.
 * **Sorting Engine:** Implements a descending sort algorithm to ensure the most resource-intensive processes remain at the top of the dashboard.
 * **Live UI:** Utilizes ANSI terminal escape codes to refresh the display in-place, preventing screen flickering and providing a smooth user experience.
## ⚠️ Limitations
 * **Permissions:** Detailed stats for certain root-level processes may be restricted unless the script is executed with administrative privileges.
 * **Display:** Optimized for standard terminal dimensions; scaling issues may occur on extremely small terminal windows.
 * **Platform:** Specifically targets the Linux kernel and /proc filesystem; not intended for Windows or macOS.
## 🛠️ Future Improvements
 * **Interactive Management:** Adding functionality to "kill" or "renice" processes directly from the dashboard using PID input.
 * **Historical Logging:** Implementing a background logger to save resource spikes to a .csv or .log file for later analysis.
 * **Networking Module:** Expanding the tracker to monitor real-time upload/download speeds per process.
 * **Alert System:** Triggering desktop notifications when CPU or RAM usage exceeds a user-defined threshold.

  📜 License
  
This project is licensed under the **MIT License**. It is free to use, modify, and distribute for personal or professional use.
