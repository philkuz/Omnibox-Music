from gmusicapi_wrapper import MobileClientWrapper
from gmusicapi import Mobileclient


def login_factory():
    data = {}
    def login(user, pwd):
        mcw = MobileClientWrapper()
        logged_in = mcw.login(user, pwd)
        if logged_in:
            data['client'] = mcw
        return logged_in
    def current_user():
        if logged_in():
            return data['client']
        else:
            return None
    def logged_in():
        return 'client' in data
    return login, logged_in, current_user

login, logged_in, current_user = login_factory()
def search_all_filters(query):
    '''
    Returns a list of tuples that searches all filter fields
    '''
    from gmusicapi_wrapper import utils
    # return [(field, query) for field in utils._get_valid_filter_fields().items()]
    return [('title', query)]
def find_url(query, num_results=5):
    '''
    Returns a dictionary mapping a song to the url, artist, and album
    Defaults to 5 results for conciseness(there is a limited number of suggestions
    you want to make in the query.
    However it's important to note that trying to request more than 100 will
    result in google servers throwing a 403  forbidden access error
    '''
    
    if num_results > 100:
        print "Can't return more than 100 results, reducing to 100"
        num_results = 100
    user = current_user()
    if user:
        matched_songs, _ = user.get_google_songs(include_filters=search_all_filters(regex(query)), all_include_filters=True)

        # songs_by_artist = {}
        saved_songs = []
        count = 0
        # TODO make this search more searchy
        for song in matched_songs:
            if count > num_results:
                break

            url = user.api.get_stream_url(song.get('id'))
            print url
            artist = song.get('artist')
            title = song.get('title')
            saved_songs.append({'url':url,'artist':artist, 'title':title})
            count += 1
            # title = song.get('title')
            # artist = song.get('artist')
            # if artist in songs_by_artist:
            #     songs_by_artist[artist].append(title)
            # else:
            #     songs_by_artist[artist] = [title]
        return saved_songs

    else:
        return False

def regex(query):
    '''
    Makes a general regex wildcard
    '''
    return query
    # return "*"+query+"*"


print find_url('Diamond')
