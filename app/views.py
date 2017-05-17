from app import app
from flask import render_template, flash, redirect,request, jsonify
from .search import callAPI
from .searchFunctions import linearSearch

@app.route('/')
def auth():
    return redirect('https://oauth.groupme.com/oauth/authorize?client_id=<CLIENT-ID???>)

@app.route('/index')
def index():
    token = request.args.get('access_token')
    #test call to API, change location of this later:x
    callAPI(token)
    return render_template("index.html")

@app.route('/search', methods = ['POST'])
def search():
    query = request.form['input']
    matches = linearSearch(query)

    if len(matches) > 0:
        return jsonify({'matches': matches})

    return jsonify({'empty': 'No messages matched your query.'})

