from flask import Flask, render_template, request, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/demo', methods=("GET","POST"))
def demo():
    if request.method == "POST":
        print(request.form["category"])

        return render_template("demo.html")
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)