import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def main():
    if len(sys.argv) != 2:
        print('[-] Error!')
        print('[+] Usage %s url' % sys.argv[0])
        print('[+] Example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print('[+] Exploiting Path traversal vulnerability')
    path_traversal_exploit(url)

if __name__ == "__main__":
    main()