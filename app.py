from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import whois_lookup
 
app = Flask(__name__)
 

 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def search():
    url=request.form['url']
    a = whois_lookup.whois_lookup(url)
    #a=whois_lookup.whois_lookup(url)
    #a={'2019-06-23 07:31:46','CYBERVIE.COM','13.126.15.3'}
    return render_template("index.html",details=a)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
