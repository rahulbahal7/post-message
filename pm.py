#! /usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(host='192.168.122.117', port=5019, debug=True)
