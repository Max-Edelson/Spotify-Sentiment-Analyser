import os
import csv
import math
from datetime import date

pathToSemiCleanedData = "../../data/cleaned_data/semi_cleaned_data.csv"
pathToSemiCleanedData2 = "../../data/cleaned_data/semi_cleaned_data2.csv"

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

def getMonthNum(m):
	month = m.lower()
	monthNum = 0
	if month == "january":
		monthNum = 1
	elif month == "february":
		monthNum = 2
	elif month == "march":
		monthNum = 3
	elif month == "april":
		monthNum = 4
	elif month == "may":
		monthNum = 5
	elif month == "june":
		monthNum = 6
	elif month == "july":
		monthNum = 7
	elif month == "august":
		monthNum = 8
	elif month == "september":
		monthNum = 9
	elif month == "october":
		monthNum = 10
	elif month == "november":
		monthNum = 11
	elif month == "december":
		monthNum = 12
	
	return monthNum

def weekFromDay(day):
	week = 0
	if day >= 1 and day <= 7:
		week = 1
	elif day >= 8 and day <= 14:
		week = 2
	elif day >= 15 and day <= 22:
		week = 3
	elif day >= 23 and day <= 31:
		week = 4
	
	return week

def getAbsDeltaDays(topY, topM, topD, releasedY, releasedM, releasedD):
	topDate = date(int(topY), int(topM), int(topD))
	releasedDate = date(int(releasedY), int(releasedM), int(releasedD))
	delta = releasedDate - topDate
	absDelta = abs(delta)
	return abs(delta.days)

def writeData(tempList):
	# write out data
	with open(pathToSemiCleanedData2, mode='w') as raw_files_combined:
		file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		for song in tempList:
			file_writer.writerow(song)

	exit()

# read in data
with open(pathToSemiCleanedData2, 'r', encoding='utf8', errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	tempSongs = []
	for each in csv_reader:
		tempSongs.append(each)

	for song in tempSongs:
		if song[INDEX_OF_RELEASE_YEAR] == "2018" or song[INDEX_OF_RELEASE_YEAR] == "2017":
			# check if we have already checked if the song is
			# acceptable to include
			releaseMonth = 0
			releaseDay = 0
			if int(song[INDEX_OF_RELEASE_MONTH]) == 0:
				print("if you would like to save and exit, enter q, otherwise enter anything else")
				if (input() == 'q'):
					writeData(tempSongs)

				# check for what month the song was released in 
				print(f"Enter month of the release of {song[INDEX_OF_NAME]} by {song[INDEX_OF_ARTIST]}")
				month = input()
				while getMonthNum(month) == 0:
					print("That was not a valid month, try again")
					month = input()
				monthNum = getMonthNum(month)
				releaseMonth = monthNum

				print(f"Enter day of the release of {song[INDEX_OF_NAME]} by {song[INDEX_OF_ARTIST]}")
				day = int(input())
				while day < 1 and day > 31:
					print("That was not a valid day, try again")
					day = int(input())
				releaseDay = day

				deltaDays = getAbsDeltaDays(song[INDEX_OF_TOP_YEAR], song[INDEX_OF_TOP_MONTH], song[INDEX_OF_TOP_FIRST_DAY], song[INDEX_OF_RELEASE_YEAR], monthNum, day)
				if int(deltaDays) > 92:
					songList.append(song)
			else:
				songList.append(song)
				releaseMonth = song[INDEX_OF_RELEASE_MONTH]
				releaseDay = song[INDEX_OF_RELEASE_DAY]
			
			tempSongCounter = 0
			tempSongs2 = tempSongs
			for eachSong in tempSongs2:
				if eachSong[INDEX_OF_NAME] == song[INDEX_OF_NAME]:
					# duplicate song
					tempSongs[tempSongCounter][INDEX_OF_RELEASE_MONTH] = releaseMonth
					tempSongs[tempSongCounter][INDEX_OF_RELEASE_DAY] = releaseDay
				tempSongCounter += 1
		else:
			songList.append(song)
	writeData(tempSongs)

