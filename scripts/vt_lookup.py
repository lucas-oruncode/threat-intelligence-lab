import argparse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3"


def get_headers():
    return {
        "x-apikey": API_KEY
    }


def lookup_hash(hash_value):
    url = f"{BASE_URL}/files/{hash_value}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        print("\n[+] Hash Analysis")
        print(f"Malicious: {stats['malicious']}")
        print(f"Suspicious: {stats['suspicious']}")
        print(f"Harmless: {stats['harmless']}")
    else:
        print("[-] Error fetching hash data")


def lookup_ip(ip):
    url = f"{BASE_URL}/ip_addresses/{ip}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        print("\n[+] IP Analysis")
        print(f"Malicious: {stats['malicious']}")
        print(f"Suspicious: {stats['suspicious']}")
        print(f"Harmless: {stats['harmless']}")
    else:
        print("[-] Error fetching IP data")


def lookup_domain(domain):
    url = f"{BASE_URL}/domains/{domain}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        print("\n[+] Domain Analysis")
        print(f"Malicious: {stats['malicious']}")
        print(f"Suspicious: {stats['suspicious']}")
        print(f"Harmless: {stats['harmless']}")
    else:
        print("[-] Error fetching domain data")


def main():
    parser = argparse.ArgumentParser(description="VirusTotal Lookup Tool")

    parser.add_argument("--hash", help="File hash (MD5/SHA256)")
    parser.add_argument("--ip", help="IP address")
    parser.add_argument("--domain", help="Domain")

    args = parser.parse_args()

    if not API_KEY:
        print("[-] API Key not found. Check your .env file.")
        return

    if args.hash:
        lookup_hash(args.hash)

    if args.ip:
        lookup_ip(args.ip)

    if args.domain:
        lookup_domain(args.domain)

    if not any([args.hash, args.ip, args.domain]):
        print("[-] Provide at least one argument: --hash, --ip or --domain")


if __name__ == "__main__":
    main()
