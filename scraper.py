import requests

<<<<<<< HEAD:main.py
URL = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(URL)
=======
url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)
>>>>>>> 19e097d8c1745d0852df52afdec044ae78e8baba:scraper.py
print(response.status_code)
