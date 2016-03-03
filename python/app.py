from flask import Flask
from motor import setSpeed
from flask import jsonify

app = Flask(__name__)

@app.route("/final/<int:speed>")
def final(speed):
    setSpeed(finalSpeed=speed)
    return jsonify({"status": "Start"})

@app.route("/delta/<int:delta>")
def delta(delta):
    setSpeed(delta=delta)
    return jsonify({"status": "Stop"})

if __name__ == "__main__":
    app.debug = True
    app.run()
