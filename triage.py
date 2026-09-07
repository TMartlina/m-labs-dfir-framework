#!/usr/bin/env python3
"""
M-Labs DFIR: M-Triage Collection Module
Automated volatile artifact extraction and forensic packaging.
Designed for rapid live-response under the OODA loop framework.
"""

import os
import shutil
import datetime

# Base evidence repository path
BASE_DIR = "/home/kali/M-Labs-DFIR/M-Triage/evidencias/"
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
case_dir = os.path.join(BASE_DIR, f"triage_{timestamp}")
os.makedirs(case_dir, exist_ok=True)


def recolectar_logs():
    """Captures the last 500 system events via journalctl."""
    output_path = os.path.join(case_dir, "journal.log")
    with open(output_path, "w") as f:
        f.write(os.popen("journalctl -n 500").read())


def recolectar_procesos():
    """Captures active running processes and execution context via ps aux."""
    output_path = os.path.join(case_dir, "procesos.txt")
    with open(output_path, "w") as f:
        f.write(os.popen("ps aux").read())


def recolectar_conexiones():
    """Captures active network sockets and listening ports via netstat -tunp."""
    output_path = os.path.join(case_dir, "conexiones.txt")
    with open(output_path, "w") as f:
        f.write(os.popen("netstat -tunp").read())


def empaquetar():
    """Compresses the gathered volatile artifacts into a structured ZIP package."""
    shutil.make_archive(case_dir, "zip", case_dir)


def ejecutar_triage():
    """Executes the full automated micro-triage workflow."""
    print("[*] Iniciando triage forense...")
    recolectar_logs()
    recolectar_procesos()
    recolectar_conexiones()
    empaquetar()
    print(f"[+] Triage completado. Evidencias empaquetadas en: {case_dir}.zip")


if __name__ == "__main__":
    ejecutar_triage()
