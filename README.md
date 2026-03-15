# Network Security Scanner & Vulnerability Finder

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A professional-grade Network Discovery and Security tool built with **Python**, **Tkinter**, and **Nmap**. This application provides an intuitive graphical interface for advanced network scanning and vulnerability assessment.

##  Features

* **Network Discovery:** Scan specific IP addresses or entire subnets (e.g., `10.150.192.1-50`).
* **Deep Port Scanning:** Identifies open ports including SSH (22), DNS (53), HTTP (80), and HTTPS (443).
* **Service Version Detection:** Leverages Nmap's engine to identify the exact software and version running on each port.
* **Vulnerability Assessment:** Integrated "Vulnerability Scan" toggle to run Nmap scripts (`--script=vuln`) for identifying known CVEs.
* **Real-time Status Bar:** Monitoring the scan progress directly from the UI.
* **Automated Reporting:** Generates a clean, persistent text report (`Net_Report.txt`) for later analysis.

##  Interface
*Dark-themed UI designed for clarity and a professional "Cyber-Security" feel.*

##  Installation & Setup

### Prerequisites
* **Python 3.14+**
* **Nmap:** Must be installed on your system. [Download Nmap here](https://nmap.org/download.html).

### Steps
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SagiStack/Network-Scanner.git](https://github.com/SagiStack/Network-Scanner.git)
   cd Network-Scanner
