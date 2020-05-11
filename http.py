import json
import urllib.request
import time
from sense_hat import SenseHat

sense = SenseHat()

url = 'http://192.168.1.3:8000'
headers = {
    'Content-Type': 'application/json',
}

while True:
    temp = int(sense.get_temperature())
    hum = int(sense.get_humidity())
    press = int(sense.get_pressure())
    data = {
        'temperature': temp,
        'humidity': hum,
        'pressure': press,
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    time.sleep(1)
