from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print("Home render request")
    return render_template("index.html")

@app.route('/login', methods=['POST'])
#@app.route('/login', methods=['GET','POST'])
def receive_data():
    print("processing req username:")
    usrname=request.form['username']
    psswrd=request.form['password']
    #return render_template("login.html")
    return f"Usuario: {usrname}\n Clave: {psswrd}"

if __name__ == "__main__":
    app.run(debug=True)

