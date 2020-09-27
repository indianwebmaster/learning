# Perform data filtering operations like one would do in SQL
import pandas as pd

reviews = pd.read_csv("ign.csv")
# print(reviews)

# print(reviews.columns)
# print(reviews.loc[0])   # first row
# print(reviews.iloc[0])  # first row
# print(reviews.head(1))  # first row
# print(reviews.iloc[:,0])  # first column

# SQL -- SELECT score_phrase FROM reviews;
# print(reviews[ ['score_phrase'] ])  # score_phrase does not be specified as a [] list, but easier as list is required for more than one (see below)

# SQL -- SELECT score_phrase, release_day FROM reviews;
# print(reviews[ ['score_phrase','release_day'] ] )

# SQL -- SELECT * from reviews where score_phrase == 'Good';
# criteria = reviews['score_phrase'] == 'Good'
# filtered_reviews = reviews[criteria]
# print(filtered_reviews)

# SQL -- SELECT * from reviews where score_phrase == 'Good' AND release_day > 15;
# criteria = (reviews['score_phrase'] == 'Good') & (reviews['release_day'] > 15)
# filtered_reviews = reviews[criteria]
# print(filtered_reviews)

# SQL -- SELECT * from reviews where score_phrase == 'Good' OR release_day > 15;
# criteria = (reviews['score_phrase'] == 'Good') | (reviews['release_day'] > 15)
# filtered_reviews = reviews[criteria]
# print(filtered_reviews)

# SQL - SELECT release_day, COUNT(*) FROM reviews GROUP BY release_day;
# print(reviews.groupby(['release_day']).size())        # Don't need the "list" as argument for groupby, but easier as it will work for multiple columns - see below.
# print(reviews.groupby(['release_day'])['release_day'].count())    # count() provides the count across ALL columns. Hence need the ['release_day'] to match the size() above
# print(reviews.groupby(['release_day'])['score_phrase'].count())     # So, count() allows you to group by one column, and count() by another. Should be same numbers as above, unless there are NaN values

# SQL - SELECT score_phrase, release_day, COUNT(*) FROM reviews GROUP BY score_phrase, release_day;
result_reviews = reviews.groupby(['score_phrase','release_day']).size()
print(result_reviews)

