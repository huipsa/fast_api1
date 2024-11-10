import requests

response = requests.post("http://127.0.0.1:8000/advertisement/",
                         json={
                             "title": "Some Deal",
                             "description": "This is a great deal.",
                             "price": 100.0,
                             "author": "Author Name"
                         }
                         )

print(response.json())

response = requests.patch("http://127.0.0.1:8000/advertisement/1", json={'price': 120.0})
print(response.json())

response = requests.delete("http://127.0.0.1:8000/advertisement/1")
print(response.json())

response = requests.get("http://127.0.0.1:8000/advertisement/1")
print(response.json())

response = requests.get("http://127.0.0.1:8000/advertisement", params={'title': 'Deal'})
print(response.json())
