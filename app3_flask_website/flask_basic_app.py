"""Basic website with flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """ Home Page """
    return "Hello Flask website"


@app.route('/about/')
def about():
    """About Page"""
    return "Demo of a Web site built using flask in python"


if __name__ == '__main__':
    app.run(debug=True)
