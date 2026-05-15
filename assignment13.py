import requests
import json
url="https://dog.ceo/dog-api/breeds-list"
response=requests.get(url)
if response.status_code==200:
    data=response.json()

 




