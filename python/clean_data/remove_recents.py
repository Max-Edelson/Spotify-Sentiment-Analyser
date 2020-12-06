import os
import csv
import math
from datetime import date

pathToSemiCleanedData2 = "../../data/cleaned_data/semi_cleaned_data2.csv"
pathToremovedRecents = "../../data/cleaned_data/clean.csv"

songList = []

# set of song titles that had their dates
# manually entered
INDEX_OF_NAME = 1
INDEX_OF_ARTIST = 2
INDEX_OF_TOP_WEEK = 4
INDEX_OF_TOP_YEAR = 5
INDEX_OF_TOP_MONTH = 6
INDEX_OF_TOP_FIRST_DAY = 7
INDEX_OF_RELEASE_YEAR = 9
INDEX_OF_RELEASE_MONTH = 10
INDEX_OF_RELEASE_DAY = 11

def getAbsDeltaDays(topY, topM, topD, releasedY, releasedM, releasedD):
	topDate = date(int(topY), int(topM), int(topD))
	releasedDate = date(int(releasedY), int(releasedM), int(releasedD))
	delta = releasedDate - topDate
	absDelta = abs(delta)
	return abs(delta.days)

# read in data
with open(pathToSemiCleanedData2, 'r', encoding='utf8', errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	songList = []

	for song in csv_reader:
		if song[INDEX_OF_RELEASE_YEAR] == "2018" or song[INDEX_OF_RELEASE_YEAR] == "2017":
			# check if we have already checked if the song is
			# acceptable to include
			deltaDays = getAbsDeltaDays(song[INDEX_OF_TOP_YEAR], song[INDEX_OF_TOP_MONTH], song[INDEX_OF_TOP_FIRST_DAY], song[INDEX_OF_RELEASE_YEAR], song[INDEX_OF_RELEASE_MONTH], song[INDEX_OF_RELEASE_DAY])
			if int(deltaDays) > 92:
				songList.append(song)
			
		else:
			songList.append(song)

# write out data
with open(pathToremovedRecents, mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for song in songList:
		file_writer.writerow(song)	
