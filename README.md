# M-Labs DFIR: Cloud & Endpoint Micro-Triage Framework

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![Cloud](https://img.shields.io/badge/AWS-EC2%20Cloud%20SOC-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)](#)
[![Focus](https://img.shields.io/badge/Architecture-DFIR%20%2F%20OODA%20Loop-blue?style=flat-square)](#)
[![Model](https://img.shields.io/badge/Service-Consulting--as--a--Service%20(CaaS)-success?style=flat-square)](#)

---

## 1. Executive Summary

Small and medium-sized enterprises (SMEs) face an asymmetric cybersecurity landscape: limited budgets, multi-cloud dependencies, and zero internal SOC teams make them prime targets for automated threats. 

Traditional digital forensics relies on Full Forensic Imaging, requiring system shutdowns and extensive downtime—a costly, post-mortem approach incompatible with modern business continuity.

M-Labs DFIR (developed under MarrufoLabs) is an automated Consulting-as-a-Service (CaaS) framework designed for rapid live-response. Operating under John Boyd's OODA Loop (Observe, Orient, Decide, Act), it replaces full-disk cloning with surgical, automated micro-triage of volatile artifacts across hybrid and cloud workloads.

---

## 2. Core Methodology: The OODA Response Architecture

The incident response lifecycle is operationalized across three coordinated tactical phases:

- **M-Readiness (Observe):** Pre-incident baseline configuration, auditing attack surface exposure, and ensuring rapid-collection readiness across endpoints.
- **M-Triage (Orient & Decide):** Automated execution of volatile telemetry acquisition scripts (`triage.py`). It gathers process trees, active socket connections, and system journals without causing service interruption.
- **M-Analysis (Act):** Deep-dive artifact correlation using specialized tooling (Volatility 3, Autopsy, Velociraptor, Wireshark) combined with behavioral profiling to ensure containment and eradicate root causes.

Continuous improvement loop: Every analyzed incident feeds telemetry and detection rules back into the M-Readiness state.

---

## 3. Laboratory Architecture & Empirical Validation

The framework was validated through multi-stage controlled intrusions across both on-premises and public cloud environments:

### Hybrid Testing Infrastructure
- **Analyst & Attacker Node:** Kali Linux (running Metasploit, Nmap, Gobuster, Hydra).
- **Target Systems:**
  - *Local Node:* Metasploitable 2 (isolated segment under VMware Workstation).
  - *Cloud Production Node:* AWS EC2 (Ubuntu Server running production web services).
- **Cloud SOC Node:** AWS EC2 (Kali Linux orchestrating remote micro-triage and telemetry).

---

## 4. Automated Micro-Triage Pipeline (triage.py)

When an alert is triggered, `triage.py` executes without third-party dependencies, capturing volatile forensic artifacts before adversary tampering:

- **System Activity:** Last 500 system events via `journalctl -n 500`.
- **Active Processes:** Snapshot of all execution contexts via `ps aux`.
- **Network Sockets:** Live TCP/UDP connections and listening sockets via `netstat -tunp`.
- **Forensic Container:** Structured, timestamped package (`triage_YYYYMMDD_HHMMSS.zip`) stored in the evidence repository preserving digital chain of custody.

---

## 5. Key Results & Incident Correlation

| Dimension | Traditional Forensics | M-Labs DFIR (CaaS) |
| :--- | :--- | :--- |
| **Downtime** | Days / Weeks (Full Imaging) | **Zero (Live Non-Invasive Triage)** |
| **Time-to-Triage** | 12–48 hours | **< 60 seconds** |
| **Evidence Scope** | Static full disk (GBs to TBs) | **Volatile high-priority artifacts (< 10 MB)** |
| **Cloud Portability**| Severely limited in multi-tenant cloud | **Native AWS EC2 / Hybrid Cloud support** |
| **Economic Viability** | Prohibitive hourly rates (€150–€300/hr) | **Lean subscription-based CaaS model** |

---

## 6. Defensive Recommendations & Roadmap

- **Telemetry Integrity:** Deploy tamper-resistant audit log shipping (`auditd` / central SIEM forwarding).
- **Identity Hardening:** Enforce MFA across all cloud administration and SSH gateways.
- **Next-Gen Evolution:** Integration of resident lightweight agents and automated anomaly detection using machine learning models.
