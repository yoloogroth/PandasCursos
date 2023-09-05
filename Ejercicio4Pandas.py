#1
 #Your code here
reviews_written = reviews.groupby('taster_twitter_handle').size()
# Check your answer
q1.check()

#2
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
# Check your answer
q2.check()

#3
price_extremes = reviews.groupby('variety').price.agg([min, max])
# Check your answer
q3.check()

#4
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
# Check your answer
q4.check()

#5
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
# Check your answer
q5.check()

#6
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
# Check your answer
q6.check()