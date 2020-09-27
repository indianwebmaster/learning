'''
pylab is a convenience module that bulk imports matplotlib.pyplot (for plotting) and numpy (for mathematics and working with arrays)
in a single name space. Although many examples use pylab, it is no longer recommended.
# import pylab as plt
'''
import numpy as np
import matplotlib.pyplot as plt

def test_histogram(ax):
    # make an array of random numbers with a gaussian reverse_distribution with
    # mean = 5.0
    # rms = 3.0
    # number of points = 1000
    data = np.random.normal(5.0, 3.0, 100)
    # make a histogram of the data array
    ax.hist(data)
    print (data)

def test_lineplot(ax):
    # Make an array of x values
    x = [1, 2, 3, 4, 5]
    # Make an array of y values for each x value
    y = [1, 4, 9, 16, 25]
    # use plots_subplots to plot x and y
    ax.plot(x, y)

def test_scatterplot(ax):
    # Make an array of x values
    x = [1, 2, 3, 4, 5]
    # Make an array of y values for each x value
    y = [3, 6, 9, 12, 15]
    # use plots_subplots to plot x and y as
    #   red circles (ro),
    #   red triangles (r^), green inverse triangles (rv), blue left triangles (r<)
    #   magenta pentagons (mp),
    #   white squares (ws)
    #   yellow diamonds (rd)
    #   purple stars (p*)
    #   red lines (r-), red diamonds and lines (rd-)
    ax.plot(x, y, 'gd-')

f,ax = plt.subplots()      # overlay
test_histogram(ax)
test_lineplot(ax)
test_scatterplot(ax)
plt.show()

f,ax = plt.subplots(3)      # 3 rows, 1 col
test_histogram(ax[0])
test_lineplot(ax[1])
test_scatterplot(ax[2])
plt.show()

f,ax = plt.subplots(2,2)    # 2 row, 2 cols
test_histogram(ax[0][0])
test_lineplot(ax[0][1])
test_scatterplot(ax[1][0])
plt.show()

f,ax = plt.subplots(3, subplot_kw=dict(projection='polar'))      # 3 rows, 1 col, polar coordinates
test_histogram(ax[0])
test_lineplot(ax[1])
test_scatterplot(ax[2])
plt.show()
