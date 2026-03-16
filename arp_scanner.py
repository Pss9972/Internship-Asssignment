import subprocess
import re

def get_arp_table():
    try:
        result = subprocess.run(
            ["arp", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout

        pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})"

        matches = re.findall(pattern, output)

        print("IP Address\tMAC Address")
        print("-----------------------------------")

        for ip, mac in matches:
            print(f"{ip}\t{mac}")

        print("\nTotal entries:", len(matches))

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== ARP Scanner ===")
    get_arp_table()