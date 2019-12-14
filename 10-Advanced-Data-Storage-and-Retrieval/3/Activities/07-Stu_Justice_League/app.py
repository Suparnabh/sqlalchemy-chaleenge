from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')


members ={'name':'Siri',
                'email':'xyz@abc.com',
                'field':'Data Science'}

@app.route('/api/v1.0/justice-league')
def justice-league():
    return jsonify(members)

if __name__ == '__main__':
    app.run(debug=True)
