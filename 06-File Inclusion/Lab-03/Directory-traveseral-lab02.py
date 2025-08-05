import sys
import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}