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
totaltracks = 0
counter = 0
playlistid = '5Za8Qpp2xP4XxhQUEqAZvd' #possibles
limit = 100
offset = 0
token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

if token:
	sp = spotipy.Spotify(auth=token)
	playlist = sp.user_playlist_tracks(username, playlistid, offset=offset, limit=limit)
	totaltracks = playlist['total']
	while counter < totaltracks:
		for track in playlist['items']:
			song = track['track'] #Track Dictionary from the Playlist item
			album = song['album'] #Album dictionary from the Track list item
			artists = song['artists'][0] #Artist diction fro the Track list item
			print u"({}) {} - {} [{}]".format(song['track_number'],artists['name'],song['name'],album['name'])
		offset += limit
		counter += limit



else:
	print "Can't get token for", username