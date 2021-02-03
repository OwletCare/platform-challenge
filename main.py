from flask import Flask
from flask_restx import Api, Resource

service_name = 'platform-challenge'
service_description = "A coding/code review challenge for platform candidates."

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title=service_name,
    description=service_description,
)
ns = api.namespace('/', description='default operations')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
