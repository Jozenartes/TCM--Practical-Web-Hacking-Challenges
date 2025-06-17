import sys
import requests
import urllib3
import urllib 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Sending the requests to burp, to able to debug, incase of an error.
proxies = {'http':'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

