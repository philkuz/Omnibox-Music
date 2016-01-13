from flask import Flask, request
from flask.ext.cors import CORS, cross_origin
from gmusicapi import Mobileclient, Musicmanager
from gmusicapi.exceptions import AlreadyLoggedIn

app = Flask(__name__)
api = Mobileclient()
# api = Musicmanager()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/search')
def search():
    query = request.args.get('query')

    return 'Hello world'
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
