from flask import Flask, render_template, request
from functions import generate_data, get_prediction
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def data():
    with open("heart.csv") as file:
        reader = csv.reader(file)
        return render_template("data.html",csv=reader)

@app.route('/research')
def research():
    return render_template("research.html")

@app.route('/demo', methods=("GET","POST"))
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)