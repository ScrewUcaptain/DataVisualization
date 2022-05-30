import matplotlib.pyplot as plt

values = range(1,1001)
squares =[i**2 for i in values]

plt.style.use("ggplot")

fig, ax = plt.subplots()


# Create a dot at x,y where x=values and y=squares
ax.scatter(values, squares, c=squares,cmap=plt.cm.Blues, s=10)
ax.axis([0, 1100, 0,1100000])

#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

plt.savefig('squares_plot.png', bbox_inches="tight")
# plt.show()
