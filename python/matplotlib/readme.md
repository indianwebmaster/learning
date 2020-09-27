- https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

> Image Components

![Image Components](components.png)

1. The Figure is the overall window or page that everything is drawn on. It’s the 
top-level component.
1. To the figure you add Axes. The Axes is the area on which the data is plotted 
with functions such as plot() and scatter() and that can have ticks, labels, 
etc. associated with it.
1. All methods of an Axes object exist as a function in the pyplot module and vice versa.
Thus, if you see `plt.xlim()`, its actually calling `ax.set_xlim()` behind the covers.
Mostly, you’ll use the functions of the pyplot module because they’re much cleaner, 
at least for simple plots, however make a habit of using the Axes object to follow proper guidelines.
1. Each Axes has the x-axis and y-axis, along with 
- major and minor tick lines and tick labels
- axis labels, titles and legend
- axis scales and gridlines
- The axis lines are termed as "spines". The top & right spines are set to invisible.

> Data
1. You can pass Python lists or numpy arrays to the plotting functions. Basically any iterable can
be passed. However, you cannot include generator functions (see learning/yield_iterables_generators)

> Basic Implementation
```python
# Just a simple line plot
import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure()

# Setup the axes (don't use add_axes(). See later for why)
# add_subplot() just defines the axes and returns the same
# 111 is actually 3 arguments, 1 row, 1 column & plot num in grid (1)
ax = fig.add_subplot(111)

# Make a line plot. args are [x-axis point],[y-axis points]
ax.plot([0,1,2,3,4,5],[10,11,12,11,11,12])

# Show all the plots added till now
plt.show()
```
- You can replace ax.plot with ax.scatter to make a "points" plot.
- Specify the figure size in inches by passing a (width x height) tuple as figsize to figure. 
> plt.figure(figsize = (3,4))
-  add_axes(rect), where rect is [x0,y0,width,height], where (x0,y0) is the absolute position
    of the left/bottom corner of the axes on the canvas (where lower left corner of the canvas
    is (0,0) ) and (width,height) defines the width and height of the axes respectively. 
    
    All the four values [x0,y0,width,height] take values between (0,1) inclusive.
    
    On the other hand, add_subplot(rcn), where rcn = 111,121,122 etc., allows matplotlib to
    auto position the plots on the canvas. 
    
    It is very rare that you would need add_axes().

- Various graphing options are
> ax.plot([x-list],[y-list]) - A simple line plot  
> ax.scatter([x-list],[y-list]) - A simple points plot  
> ax.bar([x-list],[y-list]) - A simple bar graph  
> ax.barh([x-list],[y-list]) - A simple horizontal bar graph   
> ax.axvline(x-position) - Just draw a vertical line at given x-position  
> ax.axhline(y-position) - Just draw a horizontal line at given y-position   
> ax.fill([x-list],[y-list]) - Make polygon from (x0,y0),(x1,y1),(x2,y2) ... and fill it   

- Create a legend by adding ``label="legend text"`` to the ax.plot() function and calling ``ax.legend()`` OR ``plt.legend()``
- Add a title and x/y labels to axis using ``ax.set(title="Title",xlabel="x",ylabel="y")``
- Add a title to the overall figure using ``fig.suptitle('Fig Title')`` (yes sup for super, not sub)
