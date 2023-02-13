from matplotlib import pyplot

x = range(12)
y1 = range(12)
y2 = [i**2 for i in x]
# y3,y4,...yn

pyplot.plot(x,y1)
pyplot.plot(x,y2)
pyplot.show()