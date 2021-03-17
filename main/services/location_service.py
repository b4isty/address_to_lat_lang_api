import os

import googlemaps
from dotenv import load_dotenv


class LocationService(object):
    """Location Service Class for communicating wth google map api(library)"""

    def get_lat_lng(self, address):
        """ Method to get lat and lng by address """
        gmaps = self.get_geomap_api_key()
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            geocode_result = geocode_result[0]["geometry"]["location"]
            return geocode_result
        return None

    @staticmethod
    def get_geomap_api_key():
        """Returns google map client obj"""
        load_dotenv()
        api_key = os.getenv("GOOGLE_MAP_API_KEY")
        gmaps = googlemaps.Client(key=api_key)
        return gmaps
