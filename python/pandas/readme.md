Pandas is a fantastic data-centric package for importing and analyzing data.

Some useful URLs
1. https://www.dataquest.io/blog/pandas-python-tutorial/ 
```python
import pandas as pd

reviews = pd.read_csv("ign.csv")

first_5_rows = reviews.head()
last_5_rows = reviews.tail()

num_rows_cols = reviews.shape

first_5_rows = reviews.iloc[0:5,:]  # By row indices.
first_5_rows = reviews.loc[0:5,:]   # By row labels. Default row labels == row index

reviews_without_first_column = reviews.iloc[:,1:]

score_column = reviews.loc[:,'score']
multiple_columns = reviews.loc[:,['score','release_year']]

# Another way
score_column = reviews['score']
multiple_columns = reviews[['score','release_year']]

mean_by_column = reviews.mean() # or (axis=0)
mean_by_row = reviews.mean(axis=1)

# Others like mean - min, max, media, std, count

# Read this to understand correlation
# https://www.datascience.com/blog/introduction-to-correlation-learn-data-science-tutorials
correlation_by_column = reviews.corr()

divide_score_by_2 = reviews['score']/2
# Others like / are *, +, - and ^

# Boolean operations
mean_score = reviews['score'].mean()
scores_above_or_below_mean = (reviews['score'] > mean_score)    # Each result cell = True or False
extract_above_scores = reviews[scores_above_or_below_mean]

scores_above_or_below_mean_and_platform_xbox = (reviews['score'] > mean_score) & (reviews['platform'] == 'Xbox 360')    # Each result cell = True or False
extract_above_scores = reviews[scores_above_or_below_mean_and_platform_xbox]

# Pandas also has a Dataframe plot operator
# (This section is moved to pd_plot.py)
x_axis=(reviews['platform'] == 'Xbox 360')
x_y_axis = reviews[x_axis]['score']
x_y_axis.plot(kind='hist')

extract_above_scores['score'].hist()


# Each columns is a panda Series
a_series = pd.Series([1,2,3,4])
b_series = pd.Series(['one','two','three','four'])

# This method inserts data in the dataframe by rows. Need to transpose the matrix, if the data is by columns
a_dataframe = pd.DataFrame([a_series,b_series])
ac_dataframe = pd.DataFrame([a_series,b_series]).transpose()

# Just like the method above, this method inserts data by row
b_dataframe = pd.DataFrame(
    [
        [1,2,3,4],
        ['one','two','three','four']
    ],
    index=['col1','col2']
)
# Add the .transpose() at the end to make it by column - but note the column headings have to be provided as index - as transpose happens later
bc_dataframe = pd.DataFrame(
    [
        [1,2,3,4],
        ['one','two','three','four']
    ],
    index=['col1','col2']
).transpose()
```