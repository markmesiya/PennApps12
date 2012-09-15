from dropbox import client, rest, session

APP_KEY = '1dqdv2hu6q0kzbo'
APP_SECRET = 'hol1qcixqm4d0q8'
ACCESS_TYPE = 'dropbox'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
request_token = sess.optain_request_token()

