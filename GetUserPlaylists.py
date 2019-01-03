import spotipy
import spotipy.util as util
import sys,os
import pprint
import json
import config

scope = 'playlist-read-private'
username = config.username
client_id = config.client_id
client_secret = config.client_secret
redirect_uri = 'http://mysite.com/callback/'

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

def is_json(json):
	try:
		json_object = json.loads(results)
	except ValueError, e:
		return False
	return True	

if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.user_playlists(username, limit=10, offset=25)

	print is_json(results)

	playlist = results['items']

	for item in playlist:
		playlistName = item['name']
		tracks = item['tracks'] 
		totalTracks = tracks['total']
		pid = item['id']
		print "{} - {} (Total Tracks: {})".format(playlistName, pid, totalTracks)

else:
	print "Can't get token for", username
