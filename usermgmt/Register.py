import requests

url = "http://192.168.0.29:8004/api/users/register/"
data = {"name": "punam", "phone": "7978459029", "email": "punampanigrahi3@gmail.com", "password": "punam123"}
res = requests.post(url, data=data)
print(res.json())
