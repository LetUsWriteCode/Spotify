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
limit = 100
offset = 0
trackList = ''
filename = 'Playlist.json'
f = open(filename,'w+')

token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)


def GetTrackListing(playlistId, offset, limit):
	jsonTrack = ''
	playlist = sp.user_playlist_tracks(username, playlistId, offset=offset, limit=limit)
	for track in playlist['items']:
		song = track['track'] #Track dictionary from the Playlist item, can shred later
		album = song['album'] #Album dictionary from the Track list item, can shred later
		artists = song['artists'][0] #Artist dictionary from the Track list item, can shred later
		jsonTrack += u'{{"Track": "{}", "Album": "{}", "Popularity": "{}", "Artist": "{}"}},'.format(song['name'].replace('"',''),album['name'].replace('"',''), song['popularity'],artists['name'].replace('"','')) #format JSON properly
#		jsonTrack += json.dumps({'Artist': artists['name'], 'Track': song['name'], 'Album': album['name'], 'Popularity': song['popularity']}) #Package into JSON
	return jsonTrack

if token:
	sp = spotipy.Spotify(auth=token)
	results = sp.user_playlists(username, limit=50, offset=0) 
	playlist = results['items']
	counter = 0
	jsonFile = '{"Playlists":['.encode('utf8')

	for item in playlist:
		playlistName = item['name']
		tracks = item['tracks'] 
		totalTracks = tracks['total']
		pid = item['id']

		print 'Scraping "{}" playlist'.format(playlistName)

		#If the number of tracks in the playlist is greater than the hard limit of 100 execute multiple times
		while offset < totalTracks:
			trackList += GetTrackListing(pid, offset, limit)
			offset += limit

		#Outside the tracklist call loop but inside the for playlist loop
		offset = 0 #Reset the offset to get additional tracks
		trackList = trackList[:-1] #Strip out final comma
	#jsonFile = 	u"{} - Total Tracks: {}t\ (PlaylistURI: {})".format(playlistName, totalTracks, pid)
		jsonFile += u'{{"Playlist": "{}", "Tracks": "{}", "PlaylistURI": "{}", "Tracklist": [{}]}},'.format(playlistName, totalTracks, pid, trackList)
		trackList = '' #Reset the trackList for next playlist

#	print u"{} - Total Tracks: {}t\ (PlaylistURI: {})".format(playlistName, totalTracks, pid)
#	print u'{{"Playlist": "{}", "Tracks": "{}", "PlaylistURI": "{}", "Tracklist": [{}]}}'.format(playlistName, totalTracks, pid, trackList)
#	jsonString = json.dumps({'Playlist': playlistName, 'Tracks': totalTracks, 'PlaylistURI': pid, 'Tracklist': trackList}) #Package into JSON

	jsonFile = jsonFile[:-1] #Strip out the comma for the last playlist
	jsonFile += ']}' #Close down the list and Playlist object
	f.write(jsonFile.encode('utf8'))
	f.close

else:
	print "Can't get token for", username
