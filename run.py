from flask import Flask

app = Flask(__name__)


@app.route('/<int:number>', methods=['GET'])
def index(number):
    return "even" if number % 2 == 0 else "odd"


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)
