#!/usr/bin/env python
import requests
import json

url = "https://nunite-34b5.restdb.io/rest/students-1"

payload = json.dumps( {"username": "Robert","last_name": "H"} )
headers = {
    'content-type': "application/json",
    'x-apikey': "905eeebb5594cfa05f380980a450c66c731fe",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
