import sys, json, base64

# Takes the two filenames as command line arguments
primary_playlist_name = sys.argv[1]
addition_playlist_name = sys.argv[2]

primary_playlist = json.loads(open(primary_playlist_name, 'r').read())
primary_songs = primary_playlist['songs']

addition_playlist = json.loads(open(addition_playlist_name, 'r').read())
addition_songs = addition_playlist['songs']

image = open("cover.png", "rb").read()
image_string = base64.b64encode(image).decode()

all_songs = primary_songs + addition_songs

# Remove duplicates
all_songs = [x['hash'].lower() for x in all_songs]
all_songs = set(all_songs)
all_songs = [{'songName': 'Whatever', 'hash':x} for x in all_songs]

primary_playlist['songs'] = all_songs
primary_playlist['playlistTitle'] = 'All ranked songs'
primary_playlist['playlistAuthor'] = 'PGHM'
primary_playlist['playlistDescription'] = 'All the ranked songs gathered from multiple sources in single playlist'
primary_playlist['image'] = image_string

output = open('all_ranked.bplist', 'w')
output.write(json.dumps(primary_playlist))
output.close()
