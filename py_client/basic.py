import requests
endpoint = "http://127.0.0.1:8000/api/"
response = requests.get(endpoint,data={"query":"hello world of programming"})
# print(response.text)#tihs will return the response with status code.
print(response.headers)
print(response.json())#this will return complete response with html into text format.