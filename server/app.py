#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return parameter

app.route('/count/<int:parameter>')
def count(parameter):
    count = "" 
    for element in [f'{i}\n' for i in range(parameter)]:
        count += element
    return count

app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == 'div':
        return num1 / num2
    else:
        raise ValueError

if __name__ == '__main__':
    app.run(port=5555, debug=True)
