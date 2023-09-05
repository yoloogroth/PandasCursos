#1.- dtypes
reviews.points.astype('float64')

#2.- missing data
reviews[pd.isnull(reviews.country)]
#2.1.-
reviews.region_2.fillna("Unknown")
#2.2.-
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")