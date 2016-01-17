from flask import Flask, request
from flask.ext.cors import CORS, cross_origin
from gmusicapi import Mobileclient, Musicmanager
from gmusicapi.exceptions import AlreadyLoggedIn
import local_utils as utils
import json
app = Flask(__name__)
api = Mobileclient()
# api = Musicmanager()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/search')
def search():
    '''
    the route to make search requests. Pass in query as an argument
    '''

    query = request.args.get('query')
    urls = utils.find_url(query)
    if urls:
        return json.dump(urls)
    else:
        return 'not_signed_in'
# TODO this could be configed to properly run, currently unnecessary

# @app.route('/signin',methods=['GET'])
# def signin():
#     api.perform_oauth()
#     return 'sucesss'

@app.route('/signin', methods=['GET'])
@cross_origin()
def signin():
    user = request.args.get('username')
    pwd = request.args.get('password')
    try:
        logged_in = api.login(user, pwd, Mobileclient.FROM_MAC_ADDRESS)
    except AlreadyLoggedIn:
        logged_in = True


    if logged_in:
        return 'success'
    else:
        return 'failed'


if __name__ == '__main__':
    app.run(debug=True)
