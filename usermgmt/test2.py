import json

data = '{"var1":"punu","var2":"sunu"}'

parsed = json.loads(data)
print(type(parsed))
for x, y in parsed.items():
    print(x, y)

# print(parsed.items())
