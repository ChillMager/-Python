from urllib.request import urlopen
import json
def get_ip():
    ip = json.load(urlopen('http://httpbin.org/ip'))['origin']
    return ip
