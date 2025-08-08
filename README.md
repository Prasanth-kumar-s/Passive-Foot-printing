# Passive-Foot-printing
Passive Foot Printing Toolkit is a cross-platform Python-based command-line utility that automates passive reconnaissance for a given domain. It leverages widely-used system tools and OSINT frameworks to extract valuable information without generating detectable network traffic against the target.


# Passive Foot Printing Toolkit

**Version**: 1.0  
**Author**: Prasanth-kumar-s  
**Platform**: Cross-platform (Linux, macOS, Windows)  
**Purpose**: Ethical passive reconnaissance tool for cybersecurity assessments

---

## Overview

**Passive Foot Printing** is the process of gathering publicly available information about a target (such as a domain or organization) **without directly interacting** with the target systems. It plays a crucial role in the early phases of ethical hacking, threat analysis, and red teaming by identifying exposure points before active engagement.

This toolkit automates passive reconnaissance by collecting:

- DNS information
- WHOIS registration data
- Publicly available email addresses

It uses standard OS tools like `dig`, `nslookup`, `whois`, and `theHarvester` in a clean and simplified command-line interface.

---

## Features

- Cross-platform support (Linux, macOS, Windows)
- Automatic detection of installed tools
- DNS lookups using `dig` or fallback to `nslookup`
- WHOIS information retrieval
- Email harvesting using `theHarvester` (banner suppressed)
- No direct interaction with target servers (pure OSINT)

---

## Installation

Before running the script, ensure the following dependencies are installed:

### Linux / macOS:

Open your terminal and run:

```bash
sudo apt update && sudo apt install -y dig whois theharvester
# For macOS (using Homebrew):
# brew install bind whois theharvester

git clone https://github.com/Prasanth-kumar-s/Passive-Foot-Printing.git

cd Passive-Foot-Printing

python3 passive_footprinting.py

```


When prompted, enter the domain name (e.g., example.com). The script will automatically:
	1.	Display a stylized welcome banner
	2.	Run DNS queries (dig or nslookup)
	3.	Retrieve WHOIS info
	4.	Harvest publicly listed emails using theHarvester
