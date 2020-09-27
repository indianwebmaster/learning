import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4))    # DataFrame with random numerics - 10 rows, 4 columns
print(df)

one_col = df[3]
# print(one_col)

two_cols = df.iloc[:,0:2]
# print(two_cols)

joined_df_1 = pd.concat([two_cols,one_col])
# print(joined_df_1)    # This results in 20 rows, 2 columns. 10 rows from two_cols, and 10 rows from one_col - with the 2nd col filled with NaN

joined_df_2 = two_cols.append(one_col)
# print(joined_df_2)  # Elements from one_col are added as ONE new row. So the resulting matrix is a 11 row x 10 column matrix (since one_col had
                    # 10 entries). All empty cells of this 11x10 matrix are filled with NaN.

joined_df_3 = two_cols.join(one_col)
# print(joined_df_3)  # This will add the column - so we combine a 10x2 and a 10x1 matrix to form a 10x3 matrix. This joins at the same 'row index' level.

# print(one_col)
one_col_2 = one_col.sort_values()
# print(one_col_2)
joined_df_4 = two_cols.join(one_col_2)
# print(joined_df_4)  # This will add the column - so we combine a 10x2 and a 10x1 matrix to form a 10x3 matrix. This joins at the same 'row index' level.
                    # There is no difference between joined_df_4 and joined_df_3, because the join is at the same 'row index', even though
                    # one_col was "sorted"

one_col_2 = one_col.sort_values().reset_index(drop=True)    # Reset the row indices so the 1st row is row label = 0
                                                            # drop=True means don't add the original indices as an additional column to the result. Also, obviously
                                                            # this only works for numeric row-labels
# print(one_col_2)
joined_df_5 = two_cols.join(one_col_2)
# print(joined_df_5)  # This will add the column - so we combine a 10x2 and a 10x1 matrix to form a 10x3 matrix. This joins at the same 'row index' level.
                    # This result joined_df_5 is different from _df_3 and _df_3 above, as we are resetting the index before the join.

drop_df_1 = df.drop(0, axis=1)
# print(drop_df_1)    # This drops the 0th column, but not it does not reindex the columns .... so the first column now is "column 1"
drop_df_1 = drop_df_1.T.reset_index(drop=True).T    # reset_index only works on resetting row indices. That's why you need to 'T'ranspose, reset_index and 'T' transpose back
# print(drop_df_1)

# Another way to do the "reset column numbers"
drop_df_2 = df.drop(0, axis=1)
print(drop_df_2)
drop_df_2.columns = range(drop_df_2.shape[1])
print(drop_df_2)

