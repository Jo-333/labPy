"""
=============================
Grouped bar chart with labels
=============================
This example shows a how to create a grouped bar chart and how to annotate
bars with labels.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['1A', '2A', '3A', '4A', '5A']
men_means = [26, 27, 14, 3, 15]
women_means = [7, 3, 17, 24, 15]

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='boys')
rects2 = ax.bar(x + width/2, women_means, width, label='girls')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of student')
ax.set_title('Graded and generend students')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods and classes is shown
# in this example:

matplotlib.axes.Axes.bar
matplotlib.pyplot.bar
matplotlib.axes.Axes.annotate
matplotlib.pyplot.annotate
