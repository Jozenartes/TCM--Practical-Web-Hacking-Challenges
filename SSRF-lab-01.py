import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http//127.0.0.1', 'https': 'http//127.0.0.1'}

#function that checks if the site set correclty. It requires the program to be run by adding the python version, python file and the url.
#Example: python lab-01.py www.example.com
def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Deleting Carlos user..")
    delete_user(url)

    
if __name__ == "__main__":
    main()