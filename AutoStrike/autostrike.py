import subprocess
import time
import re

BANNER = r"""
  ___  _   _ _____ _____   _____ ___________ _____ _   __ _____ 
 / _ \| | | |_   _|  _  | /  ___|_   _| ___ \_   _| | / /|  ___|
/ /_\ \ | | | | | | | | | \ `--.  | | | |_/ / | | | |/ / | |__  
|  _  | | | | | | | | | |  `--. \ | | |    /  | | |    \ |  __| 
| | | | |_| | | | \ \_/ / /\__/ / | | | |\ \ _| |_| |\  \| |___ 
\_| |_/\___/  \_/  \___/  \____/  \_/ \_| \_|\___/\_| \_/\____/  
"""

TOOLS_FILE = "tools.txt"
OUTPUT_FILE = "output.txt"

ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')

def read_tools():
    try:
        with open(TOOLS_FILE, "r") as f:
            tools = [line.strip() for line in f if line.strip()]
        return tools
    except FileNotFoundError:
        print(f"[!] {TOOLS_FILE} bulunamadı.")
        return []

def run_command_live(command, f):
    print(f"[*] {command} running...\n")
    f.write(f"[+] Command: {command}\n")
    f.flush()

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    for line in process.stdout:
        clean_line = ansi_escape.sub('', line)
        print(clean_line, end='')
        f.write(clean_line)
    f.write("\n" + "-" * 50 + "\n")
    process.wait()

def main():
    print(BANNER)
    target = input(">>> ").strip()

    tools = read_tools()
    if not tools:
        print("[!] tools.txt empty or not exist")
        return

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"{BANNER}\nTarget: {target}\n\n")
        for tool_cmd in tools:
            cmd = tool_cmd.replace("{target}", target)
            run_command_live(cmd, f)
            time.sleep(1)

    print(f"\n[✓] All tasks completed. Results '{OUTPUT_FILE}' here.")

if __name__ == "__main__":
    main()
