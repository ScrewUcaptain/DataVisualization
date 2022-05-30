import matplotlib.pyplot as plt

values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.style.use("ggplot")

fig, ax  = plt.subplots()
ax.plot(values, squares, linewidth=3)

ax.scatter(values,squares,s=120) #Create a dot at x,y where x=values and y=squares

#Set chart title and label axes.
ax.set_title("Square Numbers",fontsize=20)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Values",fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both',which="major",labelsize=14)


plt.show()