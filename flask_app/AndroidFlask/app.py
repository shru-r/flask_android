from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    d = {'username':'Shruti', 'password':'12345', 'remember me':'true'}
    return jsonify(d)

# app.run(host= '0.0.0.0')


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
