import subprocess
import time
import platform
import shutil
from colorama import init, Fore

subprocess.call("pip3 install colorama", shell=True)
# Initialize colorama
init(autoreset=True)

# Function to clear terminal
def clear_terminal():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

clear_terminal()

print(f"{Fore.YELLOW}\n [+] For Safety Please use VPN before running this script [+]")

# ASCII Art Logo
def show_logo():
    logo = f"""{Fore.CYAN}
   ____                 __  _            ______           _   _             
  / __/  ___  ___  ____/ /_(_)__  ____  /_  __/__  ____  / | / /__  ___     
 / /_   / _ \/ _ \/ __  / / / _ \/ __ \  / / / _ \/ __ \/  |/ / _ \/ _ \    
/ __/  /  __/  __/ /_/ / / /  __/ / / / / / /  __/ / / / /|  /  __/  __/    
/_/     \___/\___/\__,_/_/_/\___/_/ /_/ /_/  \___/_/ /_/_/ |_/\___/\___/     

{Fore.GREEN}[+] Passive Foot Printing Toolkit [+]
{Fore.YELLOW}[!] Author: Prasanth-kumar-s | Version: 1.0
{Fore.MAGENTA}[~] Reconnaissance script for ethical cybersecurity testing
"""
    print(logo)
    time.sleep(1)

# Tool check
def is_tool_installed(tool):
    return shutil.which(tool) is not None

# User input
domain = input(f"\n{Fore.CYAN} Enter the target Website: ").strip()

# Run dig or nslookup
def dig_or_nslookup():
    print(f"\n{Fore.GREEN} [+] Domain Information Lookup [+]")
    if is_tool_installed("dig"):
        subprocess.call(f"dig {domain}", shell=True)
    elif is_tool_installed("nslookup"):
        subprocess.call(f"nslookup {domain}", shell=True)
    else:
        print(f"{Fore.RED} [-] Neither dig nor nslookup is installed on your system.")

# Run whois
def run_whois():
    print(f"\n{Fore.GREEN} [+] Whois Information Lookup [+]")
    if is_tool_installed("whois"):
        subprocess.call(f"whois {domain}", shell=True)
    else:
        print(f"{Fore.RED} [-] whois command not found. Please install it manually.")

# Run theHarvester
def run_harvester():
    print(f"\n{Fore.GREEN} [+] Harvesting Emails [+]")
    if is_tool_installed("theHarvester"):
        # Suppress banner output by redirecting stderr to null
        if platform.system() == "Windows":
            null_output = "nul"
        else:
            null_output = "/dev/null"
        subprocess.call(f"theHarvester -d {domain} -b all -l 100 2>{null_output}", shell=True)
    else:
        print(f"{Fore.RED} [-] theHarvester is not installed.")

# Run the script
show_logo()
dig_or_nslookup()
run_whois()
run_harvester()
