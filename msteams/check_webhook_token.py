from flask import Flask
from flask import request, abort
from flask_restx import Resource, Api
from pprint import pprint as pp
import hmac
import base64
import json


app = Flask(__name__)
api = Api(app)

# SECTOKEN
SECTOKEN = 'NxEnwnWQKZqO3do4RL5X3EPlx7W8rt5BufZRJWhwghI='

def check_auth(request):
    if 'Authorization' in request.headers:
        body = request.get_data()
        digest = hmac.new(base64.b64decode(SECTOKEN.encode()), msg=body, digestmod='sha256').digest()
        signature = base64.b64encode(digest).decode()
        if f'HMAC {signature}' == request.headers['Authorization']:
            return True
    return False


@api.route('/info')
class Info(Resource):
    def post(self):
        if not check_auth(request):
            abort(401)

        print(json.dumps(request.get_json(), indent=1))
        return({'text': 'A response'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')