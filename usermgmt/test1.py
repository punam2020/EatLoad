import requests

payload = {'key1': 'value1'}
res = requests.get('https://httpbin.org/get', params=payload)
print(res.url)

# payload={'key1':'value1'}
# res=requests.post('https://httpbin.org/post',data=payload)
# print(res.text)


# cookies=dict (key1='value1')
# res=requests.get('https://httpbin.org/cookies',cookies=cookies)
# print(res.text)
