import requests as req
from flask import Flask, make_response, request
from flask_cors import CORS, cross_origin
from lxml import etree


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def hello():
    url = request.args.get('url','')
    response = req.get(url)
    
    # Parsa il contenuto XML
    root = etree.fromstring(response.content)
    
    # Namespace mapping
    namespaces = {
        'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic',
    }
    
    # Trova il valore per l'attributo 'value' con l'`id` desiderato (es. 'TIME_PERIOD')
    id_value = root.xpath("//generic:ObsValue", namespaces=namespaces)[1].get('value')
    
    # Stampa il valore ottenuto
    print("Popolazione':", id_value)

    resp = make_response(id_value)
    return resp

if __name__ == "__main__":
    app.run("localhost", 6969)



