import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http//127.0.0.1', 'https': 'http//127.0.0.1'}
