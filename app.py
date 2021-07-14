from flask import Flask, request, render_template, jsonify
from csv2db import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('front-page.html')

def generate_json(results):
    """
    Generates json from sqlalchemy results object and returns jsonify object
    """
    data = []
    """ Dictionary to hold data for json genetation """
    line = 0
    """ Current line for loop """

    if hasattr(results, 'count'):
        for row in results:
            r = [row.id, row.name ,row.address, row.postcode,  row.city,  row.license_granting_date,  row.license_type, row.business_id]
            data.insert(line, r)
            line +=1
    else:
        r = [results.id, results.name ,results.address, results.postcode,  results.city,  results.license_granting_date,  results.license_type, results.business_id]
        data.insert(line, r)

    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/all')
def api_all():
    session = Session()
    data = session.query(License).all()
    return generate_json(data)
