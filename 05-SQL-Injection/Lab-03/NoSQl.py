import requests
import string
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'https': 'http://127.0.0.1:8080', 'http': 'http://127.0.0.1:8080'}