from flask import Flask, render_template, jsonify, Response, request
from wtforms import TextField, Form

app = Flask(__name__)
NAMES = ["abc", "abcd", "abcde", "abcdef"]


class SearchForm(Form):
    autocomp = TextField('autocomp', id='autocomplete')


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


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    app.logger.debug(search)
    return jsonify(json_list=NAMES)


@app.route('/search', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
