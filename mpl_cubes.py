import matplotlib.pyplot as mpl

values = range(1, 5001)
cubes = [i**3 for i in values]

mpl.style.use('seaborn')

fig, ax = mpl.subplots()
ax.scatter(values, cubes, c=cubes, cmap=mpl.cm.YlOrRd, s=10)

ax.tick_params(axis='both', labelsize=15)

mpl.show()
