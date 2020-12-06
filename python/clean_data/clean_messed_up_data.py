import csv
pathToSemiCleanedData2 = "../../data/cleaned_data/semi_cleaned_data2.csv"

with open(pathToSemiCleanedData2, 'r', encoding='utf8', errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	actualSongs = []
	for each in csv_reader:
		if not each:
			# blank line, do nothing
			blank = 0
		elif each[0][0] == "<" or each[0][0] == ">":
			# do nothing
			blank = 0
		else:
			actualSongs.append(each)

with open(pathToSemiCleanedData2, mode='w') as raw_files_combined:
	file_writer = csv.writer(raw_files_combined, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for song in actualSongs:
		file_writer.writerow(song)
