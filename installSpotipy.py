import spotipy
import spotipy.util as util
import sys,os
import pprint
import config

scope = 'playlist-read-private'
username = config.username
client_id = config.client_id
client_secret = config.client_secret
redirect_uri = 'http://mysite.com/callback/'
filename = 'Playlist.json'
f = open(filename,'w+')

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		#artist = item['artist']
		print track['name']


if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.user_playlists(username, 2, 25)

	playlist (results)['items']
	totalTracks = (results['total'])

	for item in results['items']:
		pname = item['name']
		pid = item['id']
		print "{0} - {1} ({})".format(pname, pid, numTracks)
		tracklist = sp.user_playlist(username, item['id'], fields="tracks,next")
		show_tracks(tracks)
		while tracks['next']:
			tracks = sp.next(tracks)
			show_tracks(tracks)

else:
	print "Can't get token for", username
