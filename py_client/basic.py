import requests
endpoint = "http://127.0.0.1:8000/api/"
response = requests.get(endpoint,json={"query":"hello world of programming"})
print(response.json())#tihs will return the response with status code.
# print(response.json()["message_again"])#this will return complete response with html into text format.