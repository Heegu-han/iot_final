from flask import Flask
from flask import request
import time
app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Temperature and Humidity Data Collector</h1>"

@app.route("/temp_hum")
def collect_temp_hum():
    tm = request.args.get("tm")
    temp = request.args.get("temp")
    hum = request.args.get("hum")

    with open("temp_hum.csv","a",encoding="utf-8") as fp:
        fp.write(f"{tm},{temp},{hum}\n")

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
