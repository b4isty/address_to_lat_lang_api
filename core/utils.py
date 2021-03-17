import os

import flask
import googlemaps

from xml.dom.minidom import parseString
from dotenv import load_dotenv
from dicttoxml import dicttoxml


class Utils(object):
    """Utils Class contains common methods, required for APIs"""

    @staticmethod
    def prepare_xml_resp(data, headers=None, status=200):
        """Method to convert resp data from dict to xml format"""
        data = dicttoxml(data)
        dom = parseString(data)
        data = dom.toprettyxml()
        resp = flask.make_response(data, status)
        # if headers is being send from View, it will set that as header
        # otherwise will use the headers returned by make_response method
        if headers:
            resp.headers = headers
        resp.headers['content-type'] = 'text/xml'
        return resp
