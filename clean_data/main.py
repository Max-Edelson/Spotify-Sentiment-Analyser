import csv
import time

start_time = time.time()

pathToRawData = "../data/raw_data/"
pathToLatestData = "../data/latest_data/"
pathToCleanedData = "../data/cleaned_data/"

# array that will contain arrays of Kaggle song data
# before removing unnecessary songs
preCheckedKaggleSongs = []

# array that will hold all of our top Spotify songs
spotifySongs = []

KAGGLE_SONG_NAME_INDEX_NUMBER = 14
TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER = 1
KAGGLE_VALENCE_INDEX = 0
TOP_SPOTIFY_VALENCE_INDEX = 5
KAGGLE_ARTIST_INDEX = 3
TOP_SPOTIFY_ARTIST_INDEX = 2 
KAGGLE_DATE_INDEX = 1

# check if the song name has a 'featuring someone
# section, if it does surrounded by "()", remove it
def removeParentheses(indexOfName, row):
	foundParen = False
	charCounter = 0
	songName = row[indexOfName]
	songNameB = ""
	for char in songName:
		if foundParen:
			songNameB = songName[0:charCounter - 1]
			break;
		elif char == '(':
			foundParen = True
		charCounter += 1
	if not foundParen:
		songNameB = songName
#	songNameB = songNameB.lower()
	revisedSong = row
	revisedSong[indexOfName] = songNameB.strip()

	return revisedSong

# the Kaggle dataset gives the artists names in
# the form of an array whose contents are names
# seperated by commas, this will remove the 
# brackets, commas, and single quotation marks
def cleanArtists(indexOfArtists, row):
	cleanedArtists = []

	artists = row[indexOfArtists]
	badChars = ['[', ']', "'"]
	for char in artists:
		for i in badChars:
			artists = artists.replace(i,'')
	artists = artists.split(",")
	for artist in artists:
		artist = artist.lower()
		artist = artist.strip()
		cleanedArtists.append(artist)

	return cleanedArtists

# check if the artists match
def checkIfArtistsMatch(spotifySong, kaggleSong):
	spotifyArtist = cleanArtists(TOP_SPOTIFY_ARTIST_INDEX, spotifySong)
	kaggleArtists = cleanArtists(KAGGLE_ARTIST_INDEX, kaggleSong)

	artistsMatch = False
	for each in kaggleArtists:
		if artistsMatch:
			break
		elif each == spotifyArtist[0]:
			artistsMatch = True
	
	return artistsMatch

def checkIfSongNamesMatch(spotifySongName, kaggleSongName):
	returnVal = False
#	print(spotifySongName + " == " + kaggleSongName)
	spotName = spotifySongName.lower()
	kagName = kaggleSongName.lower()
	if spotName == kagName:
		returnVal = True
	
	return returnVal

# read in the Kaggle data and remove extranneous
# parts of the song name
with open(pathToRawData + 'kaggle_data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader :
		song = removeParentheses(KAGGLE_SONG_NAME_INDEX_NUMBER, row)
		tempRow = song
		preCheckedKaggleSongs.append(tempRow)


# read in our top Spotify songs and remove extranneous 
# parts of the song name
with open(pathToLatestData + 'raw_files_combined.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		song = removeParentheses(TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER, row)
		tempRow = song
		spotifySongs.append(tempRow)
	spotifySongs[0].append("Valence")
	spotifySongs[0].append("Release Year")

#print(spotifySongs)

# remove all songs from the Kaggle data set that aren't
# in spotifySongs, doesn't account for duplicates
# in spotifySongs and when you find a match, add in
# the valence values to the spotify songs
spotifySongCounter = 0
for each in spotifySongs:
	spotifySongCounter += 1
	kaggleSongPointer = 0
	kaggleSong = preCheckedKaggleSongs[kaggleSongPointer][KAGGLE_SONG_NAME_INDEX_NUMBER]
	spotifySong = each[TOP_SPOTIFY_SONG_NAME_INDEX_NUMBER]
	while checkIfSongNamesMatch(spotifySong, kaggleSong)  == False or checkIfArtistsMatch(each, preCheckedKaggleSongs[kaggleSongPointer]) == False:
		if kaggleSongPointer < (len(preCheckedKaggleSongs) - 1):

			kaggleSongPointer += 1
			kaggleSong = preCheckedKaggleSongs[kaggleSongPointer][KAGGLE_SONG_NAME_INDEX_NUMBER]
		else:
			break

#	if spotifySong.lower() == "havana" and kaggleSong.lower() == "havana":
#		print(preCheckedKaggleSongs[kaggleSongPointer])
	# do not add songs whose valence values are unknown
#	print(f"spotifySong: {spotifySong}, kaggleSong: {kaggleSong}, kaggleSongPointer: {kaggleSongPointer}")
	if checkIfSongNamesMatch(spotifySong, kaggleSong):
		# songs match
		kaggleValenceValue = preCheckedKaggleSongs[kaggleSongPointer][KAGGLE_VALENCE_INDEX]
		if kaggleValenceValue != '' and float(kaggleValenceValue) >= 0 and float(kaggleValenceValue) <= 1:
			each.append(kaggleValenceValue)
			each.append(preCheckedKaggleSongs[kaggleSongPointer][KAGGLE_DATE_INDEX])
	else:
#		print(f"Kaggle data set does not contain {spotifySong}")
		spotifySongs.pop(spotifySongCounter)
		continue
	if spotifySongCounter % 1000 == 0:
		print(f"done with {spotifySongCounter} songs")

# remove any songs that don't have a valence value
counter = 0
while counter < len(spotifySongs): 
	if len(spotifySongs[counter]) < 7:
		print(f"popping: {each[1]}")
		spotifySongs.pop(counter)
		counter = 0
	else:
		counter += 1


#for each in spotifySongs:
#	print(each)

# writing to a csv file
with open(pathToCleanedData + 'cleaned_data.csv', mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for song in spotifySongs:
		file_writer.writerow(song)

print("Program took %s seconds to run." % (time.time() - start_time))
