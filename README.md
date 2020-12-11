# top-spotify-songs-valence
We will analyze the top 200 listened-to songs on Spotify for each week in 2018 to find if sad songs (valence &lt; 0.4) are generally listened to in greater frequency throughout certain periods during the year.

**Spotify Valence Attributes Information**
| feature_name	| description	| type_of_data | range (numerical only) | possible values (categorical only, # of possibilities) | may contain multiple values (categorical only) |
| ---	| --- |	--- |	--- |	--- |	--- |
| position	| Ranking among weekly top 200 songs	| numerical	| 1 - 200	| -	| - |
| track_name	| Song name	| categorical	| -	| 463	| no |
| artist	| Alphabetical first artist listed for the song	| categorical	| -	| 231	| no |
| streams	| The number of streams this song had	| numerical	| 1196048 - 23636303	| -	| - |
| top_week	| Which week this song belongs too	| numerical	| 1 - 52	| -	| - |
| top_year	| What year it was when it was in the top 200	| numerical	| 2017 - 2018	| -	| - |
| top_month	| What month it was when it was in the top 200	| numerical	| 1 - 12	| -	| - |
| top_first_day	| What is the first day of the week range when it was in the top 200	| numerical	| 1 - 31	| -	| - |
| valence	| A value Spotify has assigned songs to rate their sentiment as positive or negative	| numerical	| 0.0499 - 0.979	| -	| - |
| release_year	| The year this song was released	| numerical	| 1936 - 2020	| -	| - |
| release_month	| The month this song was released	| numerical	| 1 - 12	| -	| - |
| release_day	| The day this song was released	| numerical	| 1 - 31	| -	| - |
| Total Features = 12 |					

**Songs removed from analysis**
| song_count | reason |
| --- | --- |
| 1753 | Spotify song was not present in Kaggle data set |
| 3470 | Was a top song too soon after release date (< 3 months) |
