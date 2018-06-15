from flask import Flask, request
from flask_restful import Resource, Api
import turnon
import turnoff
import time

app = Flask(__name__)
api = Api(app)

class Ping(Resource):
    def get(self):

        print "[" + time.asctime(time.localtime(time.time())) + "] Pinging..."

class Enable(Resource):
    def get(self):

        turnon.enable()

        return 'Email automation successfully turned on.'

class Disable(Resource):
    def get(self):

        turnoff.disable()

        return 'Email automation successfully turned off.'

api.add_resource(Ping, '/')
api.add_resource(Enable, '/enable')
api.add_resource(Disable, '/disable')

if __name__ == '__main__':
     app.run()
