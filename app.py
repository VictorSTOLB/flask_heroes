from flask import Flask
from flask_restful import Resource, Api

from src.resources.lib import HeroResource, HeroResourceList

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(HeroResource, '/hero', '/hero/<int:hero_id>')
api.add_resource(HeroResourceList, '/hero/list')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6969, debug=True)