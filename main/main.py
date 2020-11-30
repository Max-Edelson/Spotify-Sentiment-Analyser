import csv

# reading in from the individual weeks' csv files
numWeeks = 52
allWeekData = []
pathToRawData = "../latest_data/"

# read in data from week1 to weak52
for i in range(1, numWeeks + 1):
	with open(pathToRawData + 'week' + str(i) + '.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		weekiData = []
		columns = 5
		for row in csv_reader:
			rowI = []
			for i in range(columns):
				rowI.append(row[i])
			weekiData.append(rowI)
		allWeekData.append(weekiData)

# delete extra data
weekCounter = 0
for week in allWeekData:
	# delete the exclaimer that Spotify included in all 
	# of the raw data sets
	del week[0]

	if weekCounter != 0:
		# delete the duplicate headers
		del week[0]
	weekCounter += 1

# add week to the header
firstWeek = allWeekData[0]
firstWeek[0].append("Week")

# add a week number to each song
weekCounter = 0
for week in allWeekData:
	for song in week:
		if song[0] != "Position":
			song.append(weekCounter)
			
	weekCounter += 1

# writing to a csv file
with open(pathToRawData + 'raw_files_combined.csv', mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	weekCounter = 0
	for week in allWeekData:
		for song in week:
			file_writer.writerow(song)
