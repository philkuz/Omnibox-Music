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
@app.route('/gmusic')
def gmusic():
    '''
    Returns all songs in google music. Used to make a better search
    '''
    library = utils.all_songs()
    if library:
        return json.dump(library)
    else:
        return 'not_signed_in'

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

@app.route('/sign_in', methods=['POST'])
def signin():
    user = request.form['username']
    pwd = request.form['password']
    return json.dump(utils.login(user, pwd))



if __name__ == '__main__':
    app.run(debug=True)
