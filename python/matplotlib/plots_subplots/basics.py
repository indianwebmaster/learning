'''
    1. https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

'''
import matplotlib.pyplot as plt

def simple_plot():
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    plt.xlim(0.5, 4.5)
    plt.show()

# Same as previous, except using the Axes object instead of just the pyplot functions. More control
def simple_ax_plot():
    fig = plt.figure()
    # The 3 digit number below describes the position of the subplot
    # RCP - 1st num = num subplot Rows    2nd num = num subplot Columns     3rd num = this subplot Position
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)
    plt.show()

def two_ax_plots():
    fig = plt.figure()
    # The 3 digit number below describes the position of the subplot
    # RCP - 1st num = num subplot Rows    2nd num = num subplot Columns     3rd num = this subplot Position
    ax = fig.add_subplot(211)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    ax = fig.add_subplot(212)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    plt.show()

def two_ax_plots_one_polar():
    fig = plt.figure()
    # The 3 digit number below describes the position of the subplot
    # RCP - 1st num = num subplot Rows    2nd num = num subplot Columns     3rd num = this subplot Position
    ax = fig.add_subplot(211)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    ax = fig.add_subplot(212, polar=True)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    plt.show()

def two_ax_plots_one_polar_2():
    fig = plt.figure()
    # The 3 digit number below describes the position of the subplot
    # RCP - 1st num = num subplot Rows    2nd num = num subplot Columns     3rd num = this subplot Position
    ax = fig.add_subplot(211)
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    # Only line different from previous
    ax = fig.add_subplot(212, projection='polar')
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
    ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
    ax.set_xlim(0.5, 4.5)

    plt.show()


# simple_plot()
# simple_ax_plot()
# two_ax_plots()
# two_ax_plots_one_polar()
two_ax_plots_one_polar_2()