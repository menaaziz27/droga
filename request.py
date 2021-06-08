import requests

BASE = 'http://127.0.0.1:5000'

response = requests.put(BASE + '/drugs', {"name": "ansoline"})
# response = requests.get(BASE + '/drugs')
print(response.json())
