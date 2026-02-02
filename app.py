from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/progetti")
def progetti():
    return render_template("progetti.html")

@app.route("/competizioni")
def competizioni():
    return render_template("competizioni.html")


if (__name__ == "__main__"):
    app.run(debug=True)