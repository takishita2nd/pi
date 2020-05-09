import json
import urllib.request

url = 'http://192.168.1.3:8000'
data = {
    'foo': 123,
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()
