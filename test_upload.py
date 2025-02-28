import requests

url = 'http://127.0.0.1:8080/upload'
files = [('files', open('Safonova.m4a', 'rb')), ('files', open('examples_data_001ce26c07c20eaa0d666b824c6c6924.wav', 'rb'))]
resp = requests.post(url=url, files = files) 
print(resp.json())

