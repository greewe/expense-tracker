import requests
from urllib3 import response
headers={"PRIVATE-TOKEN": "glpat-6VAxdUQz0_kxqoS7tN6drmM6MQpvOjEKdTpucGxoNg8.01.170k7xe1f"}
response=requests.get("https://gitlab.com/api/v4/users/greewe/projects",headers=headers)
print(response.text)
print(type(response.json()))
print(response.json()[0])


