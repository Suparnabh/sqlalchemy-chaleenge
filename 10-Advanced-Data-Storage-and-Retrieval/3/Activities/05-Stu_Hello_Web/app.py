from flask import Flask

app = Flask(__name__)
#decorator

@app.route('/')
def home():
    print ('serving myfirst page')
    return('Welcome to my API!')


@app.route('/about')
def about():
        return('Suparna, Houston')

@app.route('/contact')
def contact():
        return('email at sup@gmail.com')

if __name__ == '__main__':
    app.run(debug=True)