#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAMUN X TERMINAL - Python Security Lab
A fun and educational hacker-themed terminal
Author: Mamun
Version: 2.0
"""

import os
import sys
import time
import random
import platform
import socket
import subprocess
from datetime import datetime

# ============= COLOR CODES =============
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ============= UTILITY FUNCTIONS =============

def clear():
    """Clear terminal screen"""
    os.system("clear" if os.name != "nt" else "cls")

def slow_print(text, delay=0.02):
    """Print text with typing effect"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def separator(char="-", length=50):
    """Print separator line"""
    print(GREEN + char * length + RESET)

def banner():
    """Display welcome banner"""
    clear()
    print(MAGENTA + BOLD + r"""
    ╔═════════════════════════════════════╗
    ║                                     ║
    ║    ███╗   ███╗ █████╗ ███╗   ███╗  ║
    ║    ████╗ ████║██╔══██╗████╗ ████║  ║
    ║    ██╔████╔██║███████║██╔████╔██║  ║
    ║    ██║╚██╔╝██║██╔══██║██║╚██╔╝██║  ║
    ║    ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║  ║
    ║    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ║
    ║                                     ║
    ║           X TERMINAL v2.0           ║
    ║        PYTHON SECURITY LAB          ║
    ║                                     ║
    ╚═════════════════════════════════════╝
    """ + RESET)
    
    print(CYAN + "        🔐 Welcome, Mamun! 🔐" + RESET)
    print(BLUE + "    Initializing Security Lab Terminal..." + RESET)
    separator("=", 40)
    print()

# ============= FEATURE 1: MATRIX ANIMATION =============

def matrix_animation():
    """Display matrix-style animation"""
    print(GREEN + "\n[+] MATRIX ANIMATION STARTING\n" + RESET)
    separator()
    chars = "01ABCDEF#$%&@!*"
    
    try:
        for _ in range(20):
            line = "".join(random.choice(chars) for _ in range(50))
            print(GREEN + line + RESET)
            time.sleep(0.1)
        print("\n" + GREEN + "[✓] Matrix animation complete!\n" + RESET)
    except KeyboardInterrupt:
        print(RED + "\n[!] Animation interrupted by user.\n" + RESET)

# ============= FEATURE 2: SYSTEM INFORMATION =============

def system_information():
    """Display detailed system information"""
    print(CYAN + "\n[+] DEVICE SYSTEM INFORMATION\n" + RESET)
    separator()
    
    try:
        print(f"{YELLOW}Operating System{RESET}  : {platform.system()}")
        print(f"{YELLOW}OS Release{RESET}       : {platform.release()}")
        print(f"{YELLOW}OS Version{RESET}       : {platform.version()}")
        print(f"{YELLOW}Architecture{RESET}     : {platform.machine()}")
        print(f"{YELLOW}Processor{RESET}        : {platform.processor() or 'N/A'}")
        print(f"{YELLOW}Python Version{RESET}   : {platform.python_version()}")
        print(f"{YELLOW}Device Name{RESET}      : {socket.gethostname()}")
        print(f"{YELLOW}Username{RESET}         : {os.getenv('USER', 'N/A')}")
        print(f"{YELLOW}Current Time{RESET}     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
    except Exception as e:
        print(RED + f"[!] Error: {str(e)}\n" + RESET)

# ============= FEATURE 3: PASSWORD STRENGTH CHECKER =============

def password_strength_checker():
    """Check password strength with auto-demo"""
    print(YELLOW + "\n[+] PASSWORD STRENGTH CHECKER (AUTO DEMO)\n" + RESET)
    separator()
    
    # Demo passwords
    demo_passwords = [
        "password123",
        "Mamun@2024",
        "Sec#uR1ty",
        "MyP@ssw0rd123!",
        "abc",
        "UPPERCASE123"
    ]
    
    for password in demo_passwords:
        print(f"\n{CYAN}Testing Password:{RESET} {MAGENTA}{password}{RESET}")
        print(BLUE + "-" * 40 + RESET)
        
        score = 0
        criteria = {}
        
        # Check all criteria
        criteria["Length >= 8 chars"] = len(password) >= 8
        if criteria["Length >= 8 chars"]:
            score += 1
            
        criteria["Has Lowercase"] = any(c.islower() for c in password)
        if criteria["Has Lowercase"]:
            score += 1
            
        criteria["Has Uppercase"] = any(c.isupper() for c in password)
        if criteria["Has Uppercase"]:
            score += 1
            
        criteria["Has Numbers"] = any(c.isdigit() for c in password)
        if criteria["Has Numbers"]:
            score += 1
            
        criteria["Has Special Chars"] = any(not c.isalnum() for c in password)
        if criteria["Has Special Chars"]:
            score += 1
        
        # Display results
        for criterion, passed in criteria.items():
            status = GREEN + "✓" + RESET if passed else RED + "✗" + RESET
            print(f"  {status} {criterion}")
        
        # Strength level
        print()
        if score <= 2:
            strength = RED + "WEAK" + RESET
        elif score <= 3:
            strength = YELLOW + "MEDIUM" + RESET
        elif score <= 4:
            strength = GREEN + "STRONG" + RESET
        else:
            strength = GREEN + BOLD + "VERY STRONG" + RESET
        
        print(f"Strength: {strength} ({score}/5 criteria)")
        time.sleep(0.5)
    
    print("\n" + GREEN + "[✓] Password check complete!\n" + RESET)

# ============= FEATURE 4: NETWORK INFORMATION =============

def network_information():
    """Display network and IP information"""
    print(CYAN + "\n[+] NETWORK INFORMATION\n" + RESET)
    separator()
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        print(f"{YELLOW}Hostname{RESET}     : {hostname}")
        print(f"{YELLOW}Local IP{RESET}     : {local_ip}")
        print(f"{YELLOW}Socket Family{RESET} : {socket.AF_INET}")
        
        # Try to get public info (may fail on some networks)
        try:
            print(f"{YELLOW}FQDN{RESET}         : {socket.getfqdn()}")
        except:
            pass
        
        print()
        print(YELLOW + "Note: This shows local/loopback address on most networks." + RESET)
        print()
        
    except socket.error as e:
        print(RED + f"[!] Network error: {str(e)}\n" + RESET)

# ============= FEATURE 5: SECURITY SCAN DEMO =============

def security_scan_demo():
    """Simulate a security scan"""
    print(YELLOW + "\n[+] SECURITY SCAN SIMULATION (DEMO)\n" + RESET)
    separator()
    
    print(BLUE + "⚠ This is a visual demonstration - NOT a real security scan.\n" + RESET)
    
    scans = [
        ("Loading security modules", 1.0),
        ("Initializing scanner engine", 1.2),
        ("Building threat database", 1.0),
        ("Scanning system configuration", 1.5),
        ("Checking security protocols", 1.2),
        ("Analyzing system logs", 1.3),
        ("Generating threat report", 1.0),
        ("Finalizing scan results", 0.8),
    ]
    
    for i, (task, duration) in enumerate(scans, 1):
        print(CYAN + f"[{i}] {task}" + RESET)
        time.sleep(0.3)
        print(GREEN + "    [✓] Complete\n" + RESET)
        time.sleep(duration - 0.3)
    
    print(BLUE + "─" * 40 + RESET)
    print(GREEN + "\n[✓] Security scan simulation complete!\n" + RESET)

# ============= FEATURE 6: RANDOM PASSWORD GENERATOR =============

def password_generator():
    """Generate random secure passwords"""
    print(GREEN + "\n[+] RANDOM PASSWORD GENERATOR\n" + RESET)
    separator()
    
    import string
    
    print(f"{YELLOW}Generating 5 random secure passwords...\n" + RESET)
    
    for i in range(5):
        length = random.randint(12, 16)
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        
        print(f"{CYAN}Password {i+1}:{RESET} {MAGENTA}{password}{RESET}")
        time.sleep(0.3)
    
    print("\n" + GREEN + "[✓] Passwords generated!\n" + RESET)

# ============= FEATURE 7: FILE INFO DEMO =============

def file_information_demo():
    """Display sample file information"""
    print(CYAN + "\n[+] FILE INFORMATION DEMO\n" + RESET)
    separator()
    
    files = [
        ("config.ini", 2048, "Configuration File"),
        ("database.db", 51200, "Database"),
        ("backup.zip", 1024000, "Archive"),
        ("script.py", 4096, "Python Script"),
        ("document.pdf", 256000, "PDF Document"),
        ("image.jpg", 512000, "Image File"),
    ]
    
    print(f"{YELLOW}{'Filename':<20} {'Size':<15} {'Type':<25}{RESET}")
    separator("-", 60)
    
    for filename, size, filetype in files:
        if size < 1024:
            size_str = f"{size} B"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.2f} KB"
        else:
            size_str = f"{size / (1024 * 1024):.2f} MB"
        
        print(f"{MAGENTA}{filename:<20}{RESET} {GREEN}{size_str:<15}{RESET} {CYAN}{filetype:<25}{RESET}")
        time.sleep(0.2)
    
    print("\n" + GREEN + "[✓] File information displayed!\n" + RESET)

# ============= FEATURE 8: SYSTEM RESOURCE MONITOR =============

def resource_monitor():
    """Display system resource information"""
    print(CYAN + "\n[+] SYSTEM RESOURCE MONITOR\n" + RESET)
    separator()
    
    try:
        import psutil
        
        # CPU Usage
        cpu = psutil.cpu_percent(interval=1)
        print(f"{YELLOW}CPU Usage{RESET}      : {GREEN if cpu < 50 else YELLOW if cpu < 80 else RED}{cpu}%{RESET}")
        
        # Memory Usage
        memory = psutil.virtual_memory()
        print(f"{YELLOW}Memory Usage{RESET}   : {GREEN if memory.percent < 50 else YELLOW if memory.percent < 80 else RED}{memory.percent}%{RESET}")
        print(f"{YELLOW}Memory Total{RESET}   : {memory.total / (1024**3):.2f} GB")
        print(f"{YELLOW}Memory Available{RESET} : {memory.available / (1024**3):.2f} GB")
        
        # Disk Usage
        disk = psutil.disk_usage('/')
        print(f"{YELLOW}Disk Usage{RESET}     : {GREEN if disk.percent < 50 else YELLOW if disk.percent < 80 else RED}{disk.percent}%{RESET}")
        print(f"{YELLOW}Disk Total{RESET}     : {disk.total / (1024**3):.2f} GB")
        print(f"{YELLOW}Disk Free{RESET}      : {disk.free / (1024**3):.2f} GB")
        
        print()
        
    except ImportError:
        print(YELLOW + "[!] psutil not installed. Install with: pip install psutil\n" + RESET)
    except Exception as e:
        print(RED + f"[!] Error: {str(e)}\n" + RESET)

# ============= MAIN MENU =============

def display_menu():
    """Display main menu"""
    print(CYAN + BOLD + """
╔══════════════════════════════════════════════════════════╗
║                 MAMUN X TERMINAL MENU                    ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  1.  🎬 Matrix Animation                                ║
║  2.  🖥️  System Information                              ║
║  3.  🔐 Password Strength Checker                        ║
║  4.  🌐 Network Information                              ║
║  5.  🛡️  Security Scan Demo                              ║
║  6.  🔑 Password Generator                               ║
║  7.  📁 File Information Demo                            ║
║  8.  📊 System Resource Monitor                          ║
║  9.  ℹ️  Help & Information                              ║
║  0.  🚪 Exit Terminal                                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""" + RESET)

def help_information():
    """Display help information"""
    print(CYAN + BOLD + """
╔══════════════════════════════════════════════════════════╗
║                  HELP INFORMATION                        ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  MAMUN X TERMINAL - Educational Security Lab Tool       ║
║                                                          ║
║  Features:                                               ║
║  • Matrix animation for fun visual effects              ║
║  • Display system and network information               ║
║  • Check password strength                               ║
║  • Generate secure random passwords                      ║
║  • Simulate security scans (demo only)                   ║
║  • Monitor system resources                              ║
║                                                          ║
║  Requirements:                                           ║
║  • Python 3.6+                                           ║
║  • psutil (optional, for resource monitoring)            ║
║                                                          ║
║  Installation:                                           ║
║  • pip install psutil                                    ║
║                                                          ║
║  Author: Mamun                                           ║
║  Version: 2.0                                            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""" + RESET)
    print()

# ============= MAIN FUNCTION =============

def main():
    """Main program loop"""
    banner()
    slow_print("[*] Initializing Mamun X Terminal System...", 0.02)
    time.sleep(1)
    
    while True:
        try:
            display_menu()
            choice = input(GREEN + "mamun@terminal:~$ " + RESET).strip()
            
            if choice == "1":
                matrix_animation()
            elif choice == "2":
                system_information()
            elif choice == "3":
                password_strength_checker()
            elif choice == "4":
                network_information()
            elif choice == "5":
                security_scan_demo()
            elif choice == "6":
                password_generator()
            elif choice == "7":
                file_information_demo()
            elif choice == "8":
                resource_monitor()
            elif choice == "9":
                help_information()
            elif choice == "0":
                print(GREEN + "\n[+] Thank you for using Mamun X Terminal!" + RESET)
                print(CYAN + "[+] Session closed. Goodbye, Mamun!" + RESET)
                print()
                break
            elif choice == "":
                continue
            else:
                print(RED + "\n[!] Invalid command. Please enter a valid option (0-9).\n" + RESET)
                time.sleep(0.5)
        
        except KeyboardInterrupt:
            print(RED + "\n\n[!] Terminal interrupted by user." + RESET)
            print(GREEN + "[+] Goodbye!\n" + RESET)
            break
        except Exception as e:
            print(RED + f"\n[!] Error: {str(e)}\n" + RESET)

# ============= ENTRY POINT =============

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(RED + f"\n[!] Fatal error: {str(e)}" + RESET)
        sys.exit(1)
