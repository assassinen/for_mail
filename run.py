from flask import Flask

app = Flask(__name__)


@app.route('/<int:number>', methods=['GET'])
def index(number):
    return "четное" if number % 2 == 0 else "нечетное"


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)
