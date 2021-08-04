from flask import FLask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask in a Docker container!'


if __name == '__main__':
    app.run(host='0.0.0.0', debug=True)
