import requests

url = "http://localhost:5000/api/data"  # Your own URL




# POST
data = {"key": "value"}
response = requests.post(url, json=data)
print("POST:", response.json())

# PUT
data = {"key": "new_value"}
response = requests.put(url, json=data)
print("PUT:", response.json())

# PATCH
data = {"key": "patched_value"}
response = requests.patch(url, json=data)
print("PATCH:", response.json())

# DELETE
response = requests.delete(url)
print("DELETE:", response.status_code)

# GET
response = requests.get(url, timeout=5)
print("GET:", response.json())


