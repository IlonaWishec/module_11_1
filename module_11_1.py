import requests

r = requests.get('https://requests.readthedocs.io/en/latest/index.html')

print(r.status_code)
print(r.headers['content-type'])
print(r.content[0:1000])
print(r.history)