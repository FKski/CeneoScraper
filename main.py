import requests

URL = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(URL)
print(response.status_code)
