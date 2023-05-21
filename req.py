import requests

url = "https://glauniversity.in:8085/Main/Index"

r = requests.get(url)

print(r.text)
