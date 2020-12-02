import csv

pathToRawData = "../raw_data/"
pathToLatestData = "../latest_data/"
pathToCleanedData = "../cleaned_data/"

# array that will contain arrays of Kaggle song data
kaggleSongs = []

# array that will hold all of our top Spotify songs
spotifySongs = []

KAGGLE_SONG_NAME_INDEX_NUMBER = 14
TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER = 1
KAGGLE_VALENCE_INDEX = 0
KAGGLE_ARTIST_INDEX = 3
TOP_SPOTIFY_ARTIST_INDEX = 2 

# check if the song name has a 'featuring someone
# section, if it does surrounded by "()", remove it
def removeParentheses(indexOfName, row):
	foundParen = False
	charCounter = 0
	songName = row[indexOfName]
	spotifySongName = ""
	for char in songName:
		if foundParen:
			spotifySongName = songName[0:charCounter]
		elif char == '(':
			foundParen = True
		charCounter += 1
	revisedSong = row
	revisedSong[indexOfName] = spotifySongName.strip()

	return revisedSong

# the Kaggle dataset gives the artists names in
# the form of an array whose contents are names
# seperated by commas, this will remove the 
# brackets, commas, and single quotation marks
def cleanArtists(indexOfArtists, row):
	artists = row[indexOfArtists]
	badChars = ['[', ']', "'"]
	for char in artists:
		for i in badChars:
			artists = artists.replace(i,'')
	artists = artists.split(",")
	[artist.strip() for artist in artists]
	[artist.lower() for artist in artists]

	return artists

# check if two rows are the same song
def checkIfRowsMatch(spotifyRow, kaggleRow):
	spotifyArtists = cleanArtists(TOP_SPOTIFY_ARTIST_INDEX, spotifyRow)
	kaggleArtists = cleanArtists(KAGGLE_ARTIST_INDEX, kaggleRow)

	spotifySongName = removeParentheses(TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER, spotifyRow)
	kaggleSongName = removeParentheses(KAGGLE_SONG_NAME_INDEX_NUMBER, kaggleRow)

#	print(spotifyArtists)
#	print(kaggleArtists)
#	print(spotifySongName)
#	print(kaggleSongName)

	songCounter = 1
	sameSongs = False
	for each in kaggleSongs:
		if kaggleSongName == spotifySongName:
			print("Song names are the same")
			for each in kaggleArtists:
				if each == spotifyArtists:
					sameSongs = True
					break
		songCounter += 1
	return sameSongs

# read in the Kaggle data and remove extranneous
# parts of the song name
with open(pathToRawData + 'kaggle_data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader :
		songName = removeParentheses(KAGGLE_SONG_NAME_INDEX_NUMBER, row)
		tempRow = row
		tempRow[KAGGLE_SONG_NAME_INDEX_NUMBER] = songName
		kaggleSongs.append(tempRow)


# read in our top Spotify songs and remove extranneous 
# parts of the song name
with open(pathToLatestData + 'raw_files_combined.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		songName = removeParentheses(TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER, row)
		tempRow = row
		tempRow[TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER] = songName
		spotifySongs.append(tempRow)
	spotifySongs[0].append("Valence")

# go through spotifySongs and add the valence values
for each in spotifySongs:
	for kaggleSong in kaggleSongs:
		if checkIfRowsMatch(each, kaggleSong) == True:
			each.append(kaggleSong[KAGGLE_VALENCE_INDEX])

# writing to a csv file
with open(pathToCleanedData + 'cleaned_data.csv', mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for song in spotifySongs:
		for songData in song:
			file_writer.writerow(songData)
