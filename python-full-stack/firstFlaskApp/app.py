from flask import Flask


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome Bros!!!"

@app.ruote('/store',methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>'):
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    pass

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    pass
app.run()
