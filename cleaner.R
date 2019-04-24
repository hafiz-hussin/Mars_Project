library(dplyr)
library(stringr)

data <- read.csv('./data/Mars_Weather.csv')

# selecting tweets text with daylight information (weather information)

tweets <- data %>% filter(str_detect(text, "daylight")) %>% select(text)

write.csv(tweets, file = "./data/raw_weather_tweets.csv")

# TODO: break down texts into new columns: sol, max_temp, min_temp, pressure, daylight

# TODO: convert clean csv into arff format
