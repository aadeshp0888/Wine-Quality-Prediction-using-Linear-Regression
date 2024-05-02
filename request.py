import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'density':4.8})

print(r.json())