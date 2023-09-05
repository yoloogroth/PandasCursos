#1.- 
reviews.loc[0, 'country']
#1.1.- 
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

#2.-
reviews.set_index("title")
#2.2.- 
reviews.country == 'Italy'
#2.2.3.-
reviews.loc[reviews.country == 'Italy']
#2.2.4.-
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
#2.2.5.-
reviews.loc[reviews.country.isin(['Italy', 'France'])]
#2.2.6.-
reviews.loc[reviews.price.notnull()]

#3.-
reviews['critic'] = 'everyone'
reviews['critic']

#3.3.-
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']