import matplotlib.pyplot as plt
# data to display on plots
x = [1, 2, 1, 4, 5, 6, 8, 4]
# This will plot a simple histogram
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7,8,9])
# Title to the plot
plt.title("Histogram")
# Adding the legends
plt.legend(["bar"])
plt.show()
