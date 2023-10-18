from flask import Flask, render_template, request

import random

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.route('/game', methods=["GET"])
def game():
    number = []
    for num in range(1,101):
        number.append(num)

    return render_template('game.html', number = number)


@app.route('/guess/<int:number>', methods=["GET"])
def show_number(number):
    return render_template('result.html', number = number)

if __name__ == '__main__':
    # Run the Flask web server with debugging mode turned on
    app.run(debug=True)