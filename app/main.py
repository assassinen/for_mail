from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"


@app.route('/<int:number>', methods=['GET'])
def index(number):
    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)