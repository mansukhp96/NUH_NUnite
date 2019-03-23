#!/usr/bin/env python
import requests
import json

url = "https://nunite-34b5.restdb.io/rest/students-1/5c967481307bb3000003e631"

payload = json.dumps( {
    "name": "Study Finance 3301",
    "type": "event",
    "event_type": "Study",
    "location": "Curry mezz",
    "datetime": "2019-03-23 4:00pm EDT",
    "approve_guests": "False",
    "location_hidden": "False",
    "description": "Midterm next week... :-/"
} )
headers = {
    'content-type': "application/json",
    'x-apikey': "905eeebb5594cfa05f380980a450c66c731fe",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)
