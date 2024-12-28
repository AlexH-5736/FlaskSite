import sys

from flask import render_template
from flask import Flask


app = Flask(__name__)
@app.route('/')
def index(name=None):
    return render_template('index.html', person=name)
@app.route('/lists')
def home():
    # CMS data
    cms_data = {
        "heading": "List Created Dynamically!",
        "content": [
            {"title": "Unblocked Tab", "details": "Ah yes, the unblocked tab!"},
            {"title": "ChatGPT", "details": "This will host ChatGPT."},
            {"title": "Games", "details": "Actually good unblocked games (not that scratch garbage)."},
            {"title": "Fun Things", "details": "Other fun things to do on a school Chromebook."}
        ],
        "button_text": "This Button Does Nothing!"
    }

    return render_template("newList.html", **cms_data)



if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)

