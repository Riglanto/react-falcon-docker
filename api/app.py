import falcon
from falcon.http_status import HTTPStatus

import csv
import os


def load_data():
    with open(os.path.join('data', 'data.csv')) as f:
        reader = csv.DictReader(f, delimiter='\t')
        return [{'date': row['Date'], 'yield': float(row['Yield_percent'])} for row in reader]


class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')


class DataResource:
    def on_get(self, req, resp):
        resp.media = load_data()

def create():
    api = falcon.API(middleware=[HandleCORS()])
    api.add_route('/data', DataResource())
    return api
    
api = create()
