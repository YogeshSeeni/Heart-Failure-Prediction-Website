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
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            rbp = int(request.form["rbp"])
            cholesterol = int(request.form["sc"])
            fastingBS = int(request.form["fbs"])
            maxHR = int(request.form["mhr"])
            oldPeak = float(request.form["op"])
            sex = request.form["sex"]
            chestPain = request.form["cpt"]
            restingECG = request.form["restingECG"]
            exerciseAngina = request.form["eia"]
            stSlope = request.form["stSlope"]
            inputs = [age, rbp, cholesterol, fastingBS, maxHR, oldPeak, "Normal", "ST", "ATA", "NAP", "TA", "Y", "Flat", "Up", "M"]

            for i in range(len(inputs)):
                if inputs[i] == sex or inputs[i] == chestPain or inputs[i] == restingECG or inputs[i] == exerciseAngina or inputs[i] == stSlope:
                    inputs[i] = 1

            for i in range(len(inputs)):
                if type(inputs[i]) == str:
                    inputs[i] = 0

            prediction = get_prediction(inputs)

            return render_template("demo.html", prediction=str(prediction)+"%", sex=sex, cpt=chestPain, restingECG=restingECG, eia=exerciseAngina, stSlope=stSlope)
        except Exception as e:
            print(e)
            return render_template("demo.html", prediction="Error")

    return render_template("demo.html", prediction="N/A")

if __name__ == "__main__":
    app.run(debug=True)