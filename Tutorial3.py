#1.- 
reviews.points.describe()
#1.1-
reviews.taster_name.describe()
#1.2.-
reviews.points.mean()
#1.3.-
reviews.taster_name.unique()
#1.4.-
reviews.taster_name.value_counts()

#2.- 
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
#2.1
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
#2.3
reviews.head(1)
#2.4
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
#2.5
reviews.country + " - " + reviews.region_1
