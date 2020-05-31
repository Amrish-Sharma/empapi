from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

#Setting the debug property of the app to true
app.config['DEBUG'] = True
#app.config['SERVER_NAME'] = "myapp.dev:5000"

#r = requests.get("https://api.covid19india.org/raw_data5.json")

#Welcome page
@app.route('/')
def welcome():
    r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    return render_template('index.html',data=json.loads(r.text)['data'])

@app.route('/nextpage')
def nextpage():
    return render_template('nextpage.html')

if __name__ == "__main__":
    app.run()