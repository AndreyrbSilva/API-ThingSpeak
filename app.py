from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Config do ThingSpeak
CHANNEL_ID = "2943258"
API_KEY = "G3BDQS6I5PRGFEWR"
URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?results=10"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        feeds = data["feeds"]

        labels = [feed["created_at"] for feed in feeds]
        umidade = [float(feed["field1"]) if feed["field1"] else None for feed in feeds]
        temperatura = [float(feed["field2"]) if feed["field2"] else None for feed in feeds]

        return jsonify({
            "labels": labels,
            "umidade": umidade,
            "temperatura": temperatura
        })
    else:
        return jsonify({"error": "Erro ao acessar ThingSpeak"}), 500

if __name__ == "__main__":
    app.run(debug=True)
