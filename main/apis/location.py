import flask

from flask import request
from flask_restplus.namespace import Namespace
from flask_restplus import Resource, fields

from core.utils import Utils
from main.services.location_service import LocationService

api = Namespace("Location Details", description="Location APIs")

# model to declare expected payload fields
location_model = api.model(
    "LocationModel",
    {
        "address": fields.String(
            description="Address of which you want the co-ord.", required=True
        ),
        "output_format": fields.String(
            description="Response format", enum=["json", "xml"]
        ),
    },
)


@api.route('/getAddressDetails')
class LocationAPI(Resource):
    """Location API Class for address detail"""
    def __init__(self, args):
        super(LocationAPI, self).__init__(args)
        self.location_service = LocationService()
        self.utils = Utils()

    @api.expect(location_model, validate=True)
    def post(self):
        """Post method to get address details(lat, lng)"""
        output_format = request.json["output_format"]
        address = request.json["address"]

        # accessing the data from google map api through location service
        map_api_response = self.location_service.get_lat_lng(address)
        data = {"coordinates": map_api_response,
                "address": address
                }
        # don't process the response and send 400 for no google map response
        if map_api_response:
            if output_format == "json":
                resp = flask.make_response(data, 200)
                resp.headers['content-type'] = 'application/json'
                return resp
            else:
                resp = self.utils.prepare_xml_resp(data)
                return resp

        return api.abort(400, "Please provide valid address", status="error")

    def validate_payload(self, func):
        """Check validation for required fields"""
        if not request.json.get("address"):
            return api.abort(400, "address required to get address details")
        if not request.json.get("output_format"):
            return api.abort(400, "output_format is  required('xml'/ 'json')")
