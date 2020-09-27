"""
This example showcases a sinusoidal decay animation.

class matplotlib.animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, **kwargs)
    fig: matplotlib.figure.Figure
        The figure object that is used to get draw, resize, and any other needed events
    func : callable
        The function to call at each frame. The first argument will be the next value in frames. Any additional positional arguments can be supplied via the fargs parameter.
        The required signature is:
            def func(frame, *fargs) -> iterable_of_artists:
    frames : iterable, int, generator function, or None, optional
        Source of data to pass func and each frame of the animation
        The values in frames is simply passed through to the user-supplied func and thus can be of any type.
        If an integer, then equivalent to passing range(frames)
        If a generator function, then must have the signature:
            def gen_function() -> obj
        If None, then equivalent to passing itertools.count
    init_func : callable, optional
        A function used to draw a clear frame. If not given, the results of drawing from the first item in the frames sequence will be used.
        This function will be called once before the first frame. The required signature is:
            def init_func() -> iterable_of_artists:
    fargs: tuple or None, optional
        Additional arguments to pass to each call to func
    save_count: int, optional
        The number of values from frames to cache
    interval: number, optional
        Delay between frames in milliseconds. Defaults to 200
    repeat_delay : number, optional
        If the animation in repeated, adds a delay in milliseconds before repeating the animation. Defaults to None
    repeat: bool, optional
        Controls whether the animation should repeat when the sequence of frames is completed. Defaults to True
    blit: bool, optional
        Controls whether blitting is used to optimize drawing. Defaults to False.
        If True, init_func must return an iterable of artists to be re-drawn

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define globals

# The function that is called at each frame
def run(data):
    # update the data. This is received from the data_gen generator function
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    # Extend the x-axis limits to stretch the animation horizontally
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    # Add the points to the new Line2D object
    line.set_data(xdata, ydata)

    return line,

# Generator function - or the actual equation function
# The yield call at the end implies that the function returns a value for each value of 'cnt'
# Using the 'yield' allows the function to be used in a 'for' loop to return one value
# at a time.
# Think as if the function populates all the return values in a memory list, and the
# for loop outside, gets each value from the list on each loop iteration, except the
# function does not populate a memory list - but rather just executes the function
# every time - incrementing cnt with every call to the function. Bit confusing, but
# useful when you are reading a very large file or a very large data set
def data_gen():
    cnt = 0     # Determines how data points to plot and thus how long the animation lasts
    x = -0.1
    while cnt < 200:
        cnt += 1
        x += 0.1    # 0.1 is the resolution of the graph
        # See learning/yield_iterables_generators for info on yield
        # Equation ->  y = sin(2.pi.x) * e^(-x/10)
        # so 10 defines the inverse rate of decay, higher value == lower rate of decay
        # & 2.pi defines the period of the sin-wave
        if g_use_sin_cos == "sin":
            y = np.sin(np.pi * x) * np.exp(-x / 10.)
        else:
            y = np.cos(np.pi * x) * np.exp(-x / 10.)
        yield x,y

# Initial function to clear the frame initially & with every "repeat" start
def init():
    global g_lw, g_use_sin_cos
                # Interesting, a global declaration is ONLY required for assignments, not reads of global variables
                # Since you don't change a "list variable" or "object", even if you modify a list or object attribute, it does not need global

    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(-1, 9)
    ax.figure.canvas.draw() # Needed to show the axes reset every time.

    # Need to return the same object as run()
    g_lw += 1
    if g_use_sin_cos == "sin":
        g_use_sin_cos = "cos"
        line.set_color('red')
    else:
        g_use_sin_cos = "sin"
        line.set_color('blue')
        # This will "erase" the screen and start over
        del xdata[:]
        del ydata[:]

    line.set_linewidth(g_lw)
    return line,

# Just two lists to hold the data items
xdata, ydata = [], []
# Create a figure and a set of subplots. Returns a Figure object and Axes object
fig, ax = plt.subplots()
# Given this is an animation, we create a plot with x,y as two empty lists and a line width of 2
# You need the "comma" after line because ax.plot returns a tuple with one element (Why?? don't know yet)
# The return value is a Line2D object that references the two empty lists
g_use_sin_cos="sin"
g_lw = 0
line, = ax.plot([], [], lw=g_lw)
# Toggle the grid On or Off, or specify argument 'b=True' for on.
ax.grid()
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(-1, 9)

# fig = figure object that would serve as the drawing board for the plots
# run = provides the Line2D object to be used. The line is "extended" to a new point with every call to this function
# data_gen = The (x,y) value tuple passed to the "run" function on every frame is returned by this 'generator' function
# blit = False = This is the default @ToDo what happens if I set this to True?
# @ToDo-Result - Did not see any difference
# interval=10 = Delay between frames in milliseconds. Thus defines animation speed.
# repeat=False = Well, this is designed to run forever anyway - so repeat would have no impact
# init_func=init = Initialize the data. @ToDo Do we really need this, if we move set_xlim out of this function
# @ToDo-Solved We don't need the init function, unless we have the repeat flag
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10, repeat=True, init_func=init)
# ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10, repeat=False)
plt.show()
