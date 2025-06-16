import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning())

#Sending the requests to burp, to able to debug, incase of an error.
proxies = {'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        #Correct way
        Print("[+] Example: %s www.example.com" % sys.argv[0])

if __name__ == "__main__":
    main()