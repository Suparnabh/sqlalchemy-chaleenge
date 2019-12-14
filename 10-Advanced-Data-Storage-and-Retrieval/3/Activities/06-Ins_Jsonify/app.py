from flask import Flask, jsonify

app = Flask(__name__)


about_me_dict ={'name':'Siri',
                'email':'xyz@abc.com',
                'field':'Data Science'}

@app.route('/')
def home():
    return jsonify(about_me_dict)

if __name__ == 'main':
    app.run(debug=True)

