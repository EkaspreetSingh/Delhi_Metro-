from flask import *
import sys, os
import urllib.request, json
from jinja2 import Template

template = Template("My object: {{ my_object }}")

app = Flask(__name__)
app.secret_key = "abc"

url = "https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from=Dwarka&to=Palam"

@app.route("/", methods =["GET", "POST"])
def index():
    # if request.method == "POST":
    # if "from" in request.args:
         # return render_template(url)
    return render_template('index.html')

@app.route("/path")
def route(): 
    source = request.args.get("from", "Dwarka").replace(' ','%20')
    destination = request.args.get("to", "Palam").replace(' ','%20')
    url="https://us-central1-delhimetroapi.cloudfunctions.net/route-get?from=" + source + "&to=" + destination
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    if dict['status'] != 200:
        return render_template ("faliure.html",status=dict['status']) 
    else:
        # n=len(dict['interchange']) + 1
        # prev =0 
        # for i in range(0,n):
        #     color= dict['line' + str(i + 1)] 
        #     x = findIndex(dict, dict['interchange'][i])
        #     for j in range(prev,x):
                
        #     prev = x
                
        syle = "border-color: " + dict['line1'][0] + ";"
        return render_template ("path.html", syle=syle,dict=dict)

# def findIndex(dict , str):
#     cnt=0
#     for(i in dict['path']):
#         if(i == str)
#             return cnt
#         cnt=cnt+1;
    

@app.route("/map")
def map():
    # return "hello worldd"
    return render_template('map.html')

@app.route("/test")
def test():
    return render_template('test.html')
app.run()

@app.route("/nearest")
def nearest():
    return render_template('nearest.html')

@app.route("/near_test")
def near_test():
    return render_template('near_test.html')

