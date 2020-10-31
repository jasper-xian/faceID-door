import requests


url = 'http://192.168.0.25/capture'
r = requests.get(url, allow_redirects=True)

open('unknown.jpg', 'wb').write(r.content)