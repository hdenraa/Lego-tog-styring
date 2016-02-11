from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/start")
def start():
    return jsonify({"status": "Start"})

@app.route("/stop")
def stop():
    return jsonify({"status": "Stop"})

if __name__ == "__main__":
    app.debug = True
    app.run()
