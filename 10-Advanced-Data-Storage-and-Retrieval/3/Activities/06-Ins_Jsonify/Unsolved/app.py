# @TODO import jsonify
from flask import Flask

app = Flask(__name__)

about_me_dict = {'name':'Siri',
                'field':'Data Science'}

# @TODO route and function home to return json

if __name__ == '__main__':
    app.run(debug=True)