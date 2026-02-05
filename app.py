from flask import Flask,render_template

app = Flask(__name__)
def carica_comp():
    try:
        with open('competizioni.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/progetti")
def progetti():
    return render_template("progetti.html")

@app.route("/competizioni")
def competizioni():
    competizioni = carica_comp
    return render_template("competizioni.html", competizioni=competizioni)

@app.route('/competizione/<int:comp_id>')
def dettaglio(comp_id):
    competizioni = carica_dati()
    gara = next((item for item in competizioni if item["id"] == comp_id), None)
    
    if gara is None:
        abort(404)
        
    return render_template('dettaglio_comp.html', gara=gara)


if (__name__ == "__main__"):
    app.run(debug=True)
