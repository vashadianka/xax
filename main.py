import requests
val = input("Введіть назву валюти: ")
date = input("Введіть дату: (рік, місяць, день)")
url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json"
r = requests.get(url)
if r.status_code == 200:
   data = r.json()
   print(data)
else:
   print("Помилка")