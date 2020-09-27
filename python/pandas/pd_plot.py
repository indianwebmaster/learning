import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('ign.csv')

x_axis=(reviews['platform'] == 'Xbox 360')
x_y_axis = reviews[x_axis]['score']
# x_y_axis.plot(kind='hist')

# reviews['score'].head(50).hist()

reviews['score'].head(50).plot()
reviews['score'].tail(50).plot()

plt.show(block=True)    # Without this, the plot does not stay up when run from PyCharm
