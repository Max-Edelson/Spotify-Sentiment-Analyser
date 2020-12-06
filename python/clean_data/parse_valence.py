import os
import csv
import math

pathToRemovedRecents = "../../data/cleaned_data/data_removed_recents.csv"
pathToCleanData = "../../data/cleaned_data/clean.csv"

songList = []

# set of song titles that had their dates
# manually entered
TOP_SPOTIFY_VALENCE_INDEX = 8

# read in data
with open(pathToRemovedRecents, 'r', encoding='utf8', errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	songList = []

	for song in csv_reader:
		if float(song[TOP_SPOTIFY_VALENCE_INDEX]) >= 0 and float(song[TOP_SPOTIFY_VALENCE_INDEX]) <= 0.4:
			songList.append(song)
			

# write out data
with open(pathToCleanData, mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for song in songList:
		file_writer.writerow(song)	
