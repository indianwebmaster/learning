'''
pylab is a convenience module that bulk imports matplotlib.pyplot (for plotting) and numpy (for mathematics and working with arrays)
in a single name space. Although many examples use pylab, it is no longer recommended.
# import pylab as plt
'''
import numpy as np
import matplotlib.pyplot as plt

def test_histogram():
    # make an array of random numbers with a gaussian reverse_distribution with
    # mean = 5.0
    # rms = 3.0
    # number of points = 1000
    data = np.random.normal(5.0, 3.0, 1000)
    # make a histogram of the data array
    plt.hist(data)
    print (data)
    # make plot labels
    plt.xlabel('data')
    plt.show()

def test_lineplot():
    # Make an array of x values
    x = [1, 2, 3, 4, 5]
    # Make an array of y values for each x value
    y = [1, 4, 9, 16, 25]
    # use plots_subplots to plot x and y
    plt.plot(x, y)
    # show the plot on the screen
    plt.show()

def test_scatterplot():
    # Make an array of x values
    x = [1, 2, 3, 4, 5]
    # Make an array of y values for each x value
    y = [1, 4, 9, 16, 25]
    # use plots_subplots to plot x and y as
    #   red circles (ro),
    #   red triangles (r^), green inverse triangles (rv), blue left triangles (r<)
    #   magenta pentagons (mp),
    #   white squares (ws)
    #   yellow diamonds (rd)
    #   purple stars (p*)
    #   red lines (r-), red diamonds and lines (rd-)
    plt.plot(x, y, 'gd-')
    # show the plot on the screen
    plt.show()

test_histogram()
test_lineplot()
test_scatterplot()
