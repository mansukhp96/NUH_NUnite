#!/usr/bin/env python
import requests

url = "https://nunite-34b5.restdb.io/rest/students-1"

headers = {
    'content-type': "application/json",
    'x-apikey': "905eeebb5594cfa05f380980a450c66c731fe",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
