import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    # Make a random walk
    rw = Randomwalk(500)
    rw.fill_walk()

    # style use
    plt.style.use('ggplot')

    # plot the point in the walk.
    fig, ax = plt.subplots(figsize=(15, 9))
    points_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    # ax.scatter(rw.x_values, rw.y_values,
    #            c=points_numbers, cmap=plt.cm.cividis, edgecolors='none', s=1)
    # emphasis the first and last point
    ax.scatter(0, 0, c='green', s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=25)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make an other walk ? (y/n)')
    if not keep_running.startswith('y'):
        break
