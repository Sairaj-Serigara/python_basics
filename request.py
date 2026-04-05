#DAY 89
#bs4 module

# The requests module is a popular Python library used to send HTTP requests to web servers — for example, to get data from a website or
# send data to a  web API.
import requests
# response=requests.get("https://www.google.com")
# print(response.text)
# print("\t")


import requests

url = "https://example.com/login"
data = {"username": "Sairaj", "password": "1234"}
response = requests.post(url, data=data)

# The request is sent to example.com’s server
# Specifically, the /login page (or API endpoint)
# The server receives your data (form fields)
# It processes them (e.g., checks login info)
# Then it sends a response (like “Login successful” or “Invalid password”)

