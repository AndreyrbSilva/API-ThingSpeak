import requests
import json

# Conf do Canal do ThingSpeak
CHANNEL_ID = "2943258"
API_KEY = "G3BDQS6I5PRGFEWR"

# URL da API
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?results=10"
 
# Requisição dos dados
response = requests.get(url)
 
if response.status_code == 200:
    data = response.json()
    
    print("======================== Últimos Dados Coletados ========================\n")
    for feed in data["feeds"]:
        umidade = feed["field1"]
        temperatura = feed["field2"]
        print(f"Hora: {feed['created_at']} | Umidade: {umidade}% | Temperatura: {temperatura}°C")
else:
    print("Erro ao acessar ThingSpeak:", response.status_code)