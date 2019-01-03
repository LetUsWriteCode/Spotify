import sqlite3

conn = sqlite3.connect('spotify.db')

c = conn.cursor()

def CheckTableExists(table):
	#table = "('{}',)".format(table)
	table = (table,)
	c.execute('SELECT 1 FROM sqlite_master WHERE type = "table" AND name = ?', table)
	return c.fetchone()

print """    *********************
    Building DB Objects
    *********************"""

table = ('Playlist')
if CheckTableExists(table):
	print '{} table already exists, skipped.'.format(table)
else:
	c.execute('''CREATE TABLE Playlist (PlaylistId text, Name text, Tracks smallint, PlayerURL text, ImageURL text)''')
	print 'Playlist table created'

table = ('Track')
if CheckTableExists(table):
	print '{} table already exists, skipped.'.format(table)
else:
	c.execute('''CREATE TABLE Track (TrackId int, Name text, Artist text, Album text, Popularity smallint)''')
	print 'Track table created'




#for row in c.execute('SELECT name FROM sqlite_master'):
#	print row


conn.commit()
conn.close()