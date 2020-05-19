from flask import Flask
from flask_restful import Api
from resources.data import Data

app = Flask(__name__)

api = Api(app)

api.add_resource(Data, '/data')
app.run(port=5600, debug=True)


'''
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
'''