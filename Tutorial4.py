#1.- Groupwise analysis
reviews.groupby('points').points.count()
#1.1
reviews.groupby('points').price.min()
#1.2
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
#1.3
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
#1.4
reviews.groupby(['country']).price.agg([len, min, max])

#2.- multi- indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
#2.1
mi = countries_reviewed.index
type(mi)
#2.2
countries_reviewed.reset_index()

#3.- sorting
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
#3.1.-countries_reviewed.sort_values(by='len', ascending=False)
countries_reviewed.sort_index()
#3.2
countries_reviewed.sort_values(by=['country', 'len'])