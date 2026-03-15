import tkinter as tk
import nmap
import threading
from tkinter import scrolledtext, messagebox
import os


def open_report():
    if os.path.exists("Net_Report.txt"):
        os.startfile("Net_Report.txt")
    else:
        messagebox.showwarning("Couldnt Find The Requested File")



def run_scan():
    target = entry_target.get()
    if not target:
        messagebox.showwarning("Warning", "Please enter a target IP or range!")
        return
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, f"Scanning {target}... Please wait.\n")
    btn_scan.config(state=tk.DISABLED)


    def scan_thread():
        try:
            nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
            if v_scan_var.get() == 1:
                nm.scan(target, '22,53,80,443', arguments='-sV --script=vuln')
            else:
                nm.scan(target, '22,53,80,443', arguments='-sV')
            
            text_area.insert(tk.END, "Scan Results:\n" + "="*30 + "\n")
            with open("Net_Report.txt","a",encoding="utf-8") as f:
                for host in nm.all_hosts():
                    text_area.insert(tk.END, f"\n[!] Host: {host} ({nm[host].state()})\n")
                    f.write(f"\n[!] Host: {host} ({nm[host].state()})\n")
                    for proto in nm[host].all_protocols():
                        ports = nm[host][proto].keys()
                        for port in ports:
                            s = nm[host][proto][port]
                            f.write(f" Port {port}: {s['name']} | {s['product']} {s['version']}\n")
                            text_area.insert(tk.END, f"  Port {port}: {s['name']} | {s['product']} {s['version']}\n")
            
            text_area.insert(tk.END, "\n" + "="*30 + "\nScan Finished!")
            text_area.insert(tk.END, "\n" + "Created A File Named Net_Report.txt With Full Report")
        except Exception as e:
            text_area.insert(tk.END, f"\nError: {e}")
        
        btn_scan.config(state=tk.NORMAL) 

    
    threading.Thread(target=scan_thread).start()







root = tk.Tk()
root.title("Cyber Scanner")
root.geometry("600x500")
root.configure(bg="#2c3e50") 

v_scan_var = tk.IntVar()


label_title = tk.Label(root, text="Network Security Scanner", font=("Arial", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_title.pack(pady=10)


frame_input = tk.Frame(root, bg="#2c3e50")
frame_input.pack(pady=5)

label_ip = tk.Label(frame_input, text="Target IP/Range:", bg="#2c3e50", fg="#ecf0f1")
label_ip.pack(side=tk.LEFT, padx=5)

entry_target = tk.Entry(frame_input, width=30)
entry_target.insert(0, "") 
entry_target.pack(side=tk.LEFT, padx=5)


btn_scan = tk.Button(root, text="Start Security Scan", command=run_scan, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), width=20)
btn_scan.pack(pady=10)

btn_open = tk.Button(root, text="View Full Report", command=open_report, bg="#3498db", fg="white")
btn_open.pack(pady=5)


text_area = scrolledtext.ScrolledText(root, width=70, height=15, font=("Consolas", 10), bg="#1c2833", fg="#2ecc71")
text_area.pack(pady=10, padx=10)

checkvul = tk.Checkbutton(root, text="Vulnerability Scan (Takes longer)", 
                          variable=v_scan_var, 
                          bg="#2c3e50", fg="#2ecc71", 
                          selectcolor="#1c2833", activebackground="#2c3e50")
checkvul.pack(padx=5,pady=5)

root.mainloop()
