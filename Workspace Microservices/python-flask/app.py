from flask import Flask, jsonify

app = Flask(__name__)

kids = [{'name': "Delisha",
           'age': 9,
           'order': 1},
           {'name': "Teyjansh",
           'age': 6,
           'order': 2},
           {'name': "Teyjanshee",
           'age': 5,
           'order': 3}]

@app.route('/')
def index():
    return "Welcome To The World"

@app.route("/kids", methods=['GET'])
def get():
    return jsonify({'Kids of Niranjan':kids})

@app.route("/kids/<int:order>", methods=['GET'])
def get_kid(order):
    return jsonify({'Kid': kids[order]})

@app.route("/kids", methods=['POST'])
def create():
    kid = 

if __name__ == "__main__":
    app.run(debug=True)

