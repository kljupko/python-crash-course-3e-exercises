import matplotlib.pyplot as plt
import plotly.express as px

from die import Die
from random_walk_15_5 import RandomWalk



# DICE WITH MATPLOTLIB
# --------------------

# Instantiate dice.
d1, d2 = Die(), Die()

# Roll dice.
n_rolls = 10_000
results = [d1.roll() + d2.roll() for _ in range(n_rolls)]

# Analyze rolls.
max_roll = d1.num_sides + d2.num_sides
possible_rolls = range(2, max_roll+1)
frequencies = [results.count(roll) for roll in possible_rolls]

# Draw bar chart with matplotlib.
fig, ax = plt.subplots()
ax.bar(possible_rolls, frequencies)

plt.show()



# RANDOM WALK WITH PLOTLY
# -----------------------

# Instantiate a random walk and fill it.
rw = RandomWalk()
rw.fill_walk()

# Prepare the plot.
steps = range(len(rw.x_values))

# Draw the values.
fig = px.scatter(x=rw.x_values, y=rw.y_values, color=steps,
                 color_continuous_scale='blues')

# Scale equally.
fig.update_yaxes(scaleanchor='x', scaleratio=1)

fig.show()
