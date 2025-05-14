from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Merhaba! Flask API GitHub’a başarıyla yüklenecek."), 200

if __name__ == "__main__":
    app.run(debug=True)
