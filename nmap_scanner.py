import subprocess

NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"

def check_nmap():
    try:
        subprocess.run([NMAP_PATH, "--version"], stdout=subprocess.PIPE)
        return True
    except:
        return False


def run_scan(target):
    try:
        result = subprocess.run(
            [NMAP_PATH, target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    print("=== Nmap Scanner ===")

    if not check_nmap():
        print("Nmap is not installed")
        exit()

    target = input("Enter target IP: ")
    run_scan(target)