from flask import Flask, render_template, request, jsonify
import user,security
from security import authenticate

app = Flask(__name__)
@app.route('/auth')
def auth():
    return render_template('index.html')

@app.route('/landing',methods=['POST'])
def landing():
    if authenticate(request.form["username"],request.form["password"]):
        return jsonify({"message":"Authenticated"})
    else:
        return jsonify({"message":"Authentication Failed!!!"})


app.run(debug=True)
