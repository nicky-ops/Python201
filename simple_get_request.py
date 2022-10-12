# import requests

# req = requests.get("https://reclientdigital.com")
# print(req.status_code)

# SIMPLE SITE MONITORING SCRIPT
import requests
import time
while True:
    req = requests.get("https://reclientdigital.com")
    print(req.status_code)
    if req.status_code != 200:
        pass
    time.sleep(0)