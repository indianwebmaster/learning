'''
- A pandas dataframe is a way to store data in a "grid" format.
- Dataframe is defined as a 2-D data structure with columns of potentially different data types
- Dataframe has 3 components - the columns, the (row) index and the data
- The data can be
    - Another dataframe (thus making a complex structure)
    - a Panda Series (a 1-D data structure, which is what a single dataframe column is)
    - a numpy array (ndarry)
'''
import pandas as pd

reviews = pd.read_csv("ign.csv")

first_5_rows = reviews.head()
print(first_5_rows)
last_5_rows = reviews.tail()
print(last_5_rows)

num_rows_cols = reviews.shape
print(num_rows_cols)

first_5_rows = reviews.iloc[0:5,:]  # By row indices.
print(first_5_rows)
first_5_rows = reviews.loc[0:5,:]   # By row labels. Default row labels == row index
print(first_5_rows)

reviews_without_first_column = reviews.iloc[:,1:]
print(reviews_without_first_column.head())

score_column = reviews.loc[:,'score']
print(score_column.head())
multiple_columns = reviews.loc[:,['score','release_year']]
print(multiple_columns.head())

# Another way
score_column = reviews['score']
print(score_column.head())
multiple_columns = reviews[['score','release_year']]
print(multiple_columns.head())

mean_by_column = reviews.mean() # or (axis=0)
print(mean_by_column)
mean_by_row = reviews.mean(axis=1)
print(mean_by_row)

# Others like mean - min, max, media, std, count

# Read this to understand correlation
# https://www.datascience.com/blog/introduction-to-correlation-learn-data-science-tutorials
correlation_by_column = reviews.corr()
print(correlation_by_column)

divide_score_by_2 = reviews['score']/2
print(divide_score_by_2)
# Others like / are *, +, - and ^

# Boolean operations
mean_score = reviews['score'].mean()
scores_above_or_below_mean = (reviews['score'] > mean_score)    # Each result cell = True or False
print(scores_above_or_below_mean)
extract_above_scores = reviews[scores_above_or_below_mean]
print(extract_above_scores)

scores_above_or_below_mean_and_platform_xbox = (reviews['score'] > mean_score) & (reviews['platform'] == 'Xbox 360')    # Each result cell = True or False
print(scores_above_or_below_mean_and_platform_xbox)
extract_above_scores = reviews[scores_above_or_below_mean_and_platform_xbox]
print(extract_above_scores['score'])

# Pandas also has a Dataframe plot operator
x_axis=(reviews['platform'] == 'Xbox 360')
x_y_axis = reviews[x_axis]['score']
x_y_axis.plot(kind='hist')

reviews['score'].hist()

# Each columns is a panda Series
a_series = pd.Series([1,2,3,4])
print(a_series.head())
b_series = pd.Series(['one','two','three','four'])
print(b_series.tail())

# This method inserts data in the dataframe by rows. Need to transpose the matrix, if the data is by columns
a_dataframe = pd.DataFrame([a_series,b_series])
print(a_dataframe)
ac_dataframe = pd.DataFrame([a_series,b_series]).transpose()
print(ac_dataframe)

# Just like the method above, this method inserts data by row
b_dataframe = pd.DataFrame(
    [
        [1,2,3,4],
        ['one','two','three','four']
    ],
    index=['col1','col2']
)
print(b_dataframe)
# Add the .transpose() at the end to make it by column - but note the column headings have to be provided as index - as transpose happens later
bc_dataframe = pd.DataFrame(
    [
        [1,2,3,4],
        ['one','two','three','four']
    ],
    index=['col1','col2']
).transpose()
print(bc_dataframe)
