import requests as req
import xmltodict
from flask import Flask, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def hello():
    url = req.GET.get('url')
    response = req.get(url)
    data = xmltodict.parse(response.content)    
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return response.json()

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
#     return text

if __name__ == "__main__":
    app.run("localhost", 6969)



