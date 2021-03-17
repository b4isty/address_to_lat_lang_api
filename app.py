import os
from flask_restplus import Api
from main.apis.location import api as location_api
from main import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

api = Api(app, version='1.0', title='Verloop Assignment API Docs',
          description='List of APIs for Verloop Assignment.',
          doc='/docs'
          )

# Endpoints
api.add_namespace(location_api, path='/v1')

# Run Server
if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', 5000)
    app.run(host=host, port=port)
