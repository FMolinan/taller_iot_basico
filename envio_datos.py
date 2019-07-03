import requests

payload = {
    'marco': 'polo!'
}

res = requests.post('http://localhost:5000/echo', json=payload)
if res.ok:
    print(res.json())