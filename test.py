import requests

url="http://127.0.0.1:8000/user"


req= requests.get(url)

reponse=req.json()

for user in reponse:

    print(f"bonjour : {user['name']}")