from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)



@app.route('/')
def home():
    return 'Hello World'

@app.route('/greeting')
def greeting():
    return render_template('greetings.html', name='Kobe')

ingredients = ['cherry', 'blueberry', 'huckleberry']


@app.route('/pie', methods=['GET'])
def pie():
    return jsonify({'ingredients': random.choice(ingredients)})

if __name__ == '__main__':
    app.run()
