
# Valerie Walsh 24-04-2018
# Iris Data Set project

# Attempting to make a 3D Scatter plot
# Was unable to create via the iris file so based it on the random output
# Set the range between 0-50
# Ref: https://stackoverflow.com/questions/1985856/how-to-make-a-3d-scatter-plot-in-python

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = list(range(0, 50))
sequence_containing_y_vals = list(range(0, 50))
sequence_containing_z_vals = list(range(0, 50))

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()
