import pandas as pd

#1.- simple Dataframe 
print("simple dataframe")
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

#2.- simple dataframe example 2
print("example dataframe 2 ")
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#3.- example series 
print("simple series")
pd.Series([1, 2, 3, 4, 5])

#4.- series a single column of a dataframe 
print("simple siere a single column of a dataframe")
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#5.- reading data files
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

wine_reviews.head()