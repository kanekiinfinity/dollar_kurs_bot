import requests
from pprint import pprint as print


API_KEY = '1ebdc6437ef872834609ded0'

birlik = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{birlik}/UZS"

response = requests.get(url)


sana = response.json()['time_last_update_utc']

kurs = response.json()['conversion_rate']
