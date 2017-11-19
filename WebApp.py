from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("stocks.html")


@app.route('/stocks')
def stocks():
    return render_template("stocks.json")


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(debug=True)
