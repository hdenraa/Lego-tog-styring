from flask import Flask
from motor import setSpeed
from flask import jsonify

app = Flask(__name__)

@app.route("/final/<int:speed>")
def final(speed):
    return jsonify({"speed": setSpeed(finalSpeed=speed)})

@app.route("/delta/<delta>")
def delta(delta):
    return jsonify({"speed": setSpeed(delta=int(delta))})

@app.route("/stop")
def stop():
    setSpeed(finalSpeed=0)
    return jsonify({"speed": 0})

if __name__ == "__main__":
    app.debug = True
    app.run()
