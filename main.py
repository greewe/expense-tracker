import requests
from urllib3 import response


response=requests.get("https://gitlab.com/api/v4/users/greewe/projects",headers=headers)
print(response.text)
print(type(response.json()))
print(response.json()[0])


