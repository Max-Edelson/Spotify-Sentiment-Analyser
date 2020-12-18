#Program for analyzing the data in clean.csv for weeks

#Use R default packages
library(datasets)

#Use ggplot2 for graphs
library(ggplot2)


#Use spotifyData object to work with data
spotifyData <- read.csv("clean.csv", TRUE, ",")

#file with no songs omitted
spotifyRawData <- read.csv("raw_files_combined.csv", TRUE, ",")

#Find the number of songs in each week with a valence < 0.4
for(i in 1:52){
print(length(spotifyData$valence[spotifyData$valence < 0.4
                            & spotifyData$top_week == i]))
}

#number of songs per week with valence < 0.4
numSongsPerWeek <- read.csv("descriptive_data_analysis.csv", TRUE, ",")


#Create line plot of the percent of the number of sad songs per week with a 
#valence of < 0.4
ggplot(data = numSongsPerWeek, aes(x = ï..week, y = ratio, group = 1)) +
  geom_line(color = "dark green", size = 1.2) +
  ggtitle(label = "Percent of Sad Songs Per Week",
          subtitle = "Percent of songs that have a valence less than 0.4 in the top 200 songs on Spotify each week in 2018") +
  labs(y = "Percent of Sad Songs", x = "Week") +
   scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor.y = element_line(size=3),
        panel.grid.major = element_line(colour = "black")) 


#output mean of valence for songs with < 0.4 valence per week
for (i in 1:52) {
  print(summary(spotifyData$valence[spotifyData$valence < 0.4
                                    & spotifyData$top_week == i]), file = "testing.csv")
  
}


#output number of streams each week of sad songs
for(i in 1:52){
  print(sum(spotifyData$streams[spotifyData$valence < 0.4
                                   & spotifyData$top_week == i]))
}

#output number of streams each week
for(i in 1:52){
  print(sum(spotifyRawData$Streams[spotifyRawData$Week == i]))
}

#Like graph for the percent of sad songs streamed per week
ggplot(data = numSongsPerWeek, aes(x = ï..week)) +
  
  geom_line(aes(y = ratio_of_sad_song_streams), color = "dark green", size = 1.2) +
  #geom_line(aes(y = total_streams), color = "gray", size = 1.2) +
  ggtitle(label = "Percent of Sad Songs Streamed Per Week",
          subtitle = "Percent of sad songs streamed was calculated by dividing the number of streams of sad songs by the total number of streams that week") +
  labs(y = "Percent of Sad Songs Streamed", x = "Week") +
  scale_y_continuous(labels = scales::percent, limits = c(0, 0.3)) +
  theme(panel.background = element_rect(fill = 'white'),
        panel.grid.minor.y = element_line(size=3),
        panel.grid.major = element_line(colour = "black"))









