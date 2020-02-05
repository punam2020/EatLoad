import requests

# url="http://www.google.com"
# response=requests.get(url)
# print(response.status_code)


url = "http://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.text
print(type(data))
data = response.json()
print(data)
