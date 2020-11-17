""" Falsk app with html templates """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """ Home Page """
    return render_template("home.html")


@app.route("/about")
def about():
    """ About Page"""
    return render_template("about.html")


def main():
    """ The main entry """
    app.run(debug=True)


if __name__ == '__main__':
    main()
