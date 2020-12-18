#Program for analyzing the data in clean.csv for months

#Use R default packages
library(datasets)

#Use ggplot2 for graphs
library(ggplot2)


#Use spotifyData object to work with data
spotifyData <- read.csv("clean.csv", TRUE, ",")

#file with no songs omitted
spotifyRawData <- read.csv("raw_files_combined.csv", TRUE, ",")

#Find the number of songs in each month with a valence < 0.4
for(i in 1:12){
  print(length(spotifyData$valence[spotifyData$valence < 0.4
                                   & spotifyData$top_month == i]))
}

#number of songs per month with valence < 0.4
numSongsPerMonth <- read.csv("descriptive_data_analysis_months.csv", TRUE, ",")

#order the months starting from January
numSongsPerMonth$ï..month <- factor(numSongsPerMonth$ï..month, levels=c("January", "February", "March", "April", "May", "June", "July", "August",
                                                            "September", "October", "November", "December"))


#Create line graph of the percent of the number of sad songs per month with a 
#valence of < 0.4
ggplot(data = numSongsPerMonth, aes(x = ï..month , y = ratio, group = 1)) +
  geom_line(color = "dark green", size = 1.2) +
  ggtitle(label = "Percent of Sad Songs Played Per Month",
          subtitle = "Percent of songs that have a valence less than 0.4 in the top 200 songs on Spotify each month in 2018") +
  labs(y = "Percent of Sad Songs", x = "Month") +
  scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor.y = element_line(size=3),
        panel.grid.major = element_line(colour = "black")) 


#Bar chart for the percent of the number of sad songs per month with a 
#valence of < 0.4
ggplot(data = numSongsPerMonth, aes(x = ï..month , y = ratio, group = 1)) + 
  geom_bar(stat = "identity", color="blue", fill=rgb(0.1,0.4,0.5,0.7)) +
scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor = element_line(color = "black"),
        panel.grid.major = element_blank()) +
  labs(y = "Percent of Sad Songs", x = "Month") + 
  ggtitle(label = "Percent of Sad Songs Played Per Month",
          subtitle = "Percent of songs that have a valence less than 0.4 in the top 200 songs on Spotify each month in 2018") 


#output mean of valence for songs with < 0.4 valence per month
for (i in 1:12) {
  print(summary(spotifyData$valence[spotifyData$valence < 0.4
                                    & spotifyData$top_month == i]), file = "testing.csv")
}

#output number of streams each month of sad songs
for(i in 1:12){
  print(sum(spotifyData$streams[spotifyData$valence < 0.4
                                & spotifyData$top_month == i]))
}

#output number of streams each month
for(i in 1:12){
  print(sum(spotifyRawData$Streams[spotifyRawData$Month == i]))
}

#Like graph for the percent of sad songs streamed per month
ggplot(data = numSongsPerMonth, aes(x = ï..month , y = ratio_of_sad_song_streams, group = 1)) +
  geom_line(color = "dark green", size = 1.2) +
  ggtitle(label = "Percent of Sad Songs Streamed Per Month",
          subtitle = "Percent of sad songs streamed was calculated by dividing the number of streams of sad songs by the total number of streams that month") +
  labs(y = "Percent of Sad Songs Streamed", x = "Month") +
  scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor.y = element_line(size=3),
        panel.grid.major = element_line(colour = "black")) 

#Bar chart for the percent of sad songs streamed per month
ggplot(data = numSongsPerMonth, aes(x = ï..month , y = ratio_of_sad_song_streams, group = 1)) + 
  geom_bar(stat = "identity", color="blue", fill=rgb(0.1,0.4,0.5,0.7)) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor = element_line(color = "black"),
        panel.grid.major = element_blank()) +
  labs(y = "Percent of Sad Songs", x = "Month") + 
  ggtitle(label = "Percent of Sad Songs Streamed Per Month",
          subtitle = "Percent of sad songs streamed was calculated by dividing the number of streams of sad songs by the total number of streams that month") 
