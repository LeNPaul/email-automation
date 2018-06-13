from flask import Flask, request
from flask_restful import Resource, Api
import turnon
import turnoff

app = Flask(__name__)
api = Api(app)

class Enable(Resource):
    def get(self):

        turnon.enable()

        return 'Turning on.'

class Disable(Resource):
    def get(self):

        turnoff.disable()

        return 'Turning off'

api.add_resource(Enable, '/enable')
api.add_resource(Disable, '/disable')

if __name__ == '__main__':
     app.run()
