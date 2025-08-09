import plotly.express as px

from die import Die

# Create two D8s.
d1, d2 = Die(8), Die(8)

# Generate rolls.
results = []
rolls = 1_000_000
for _ in range(rolls):
    result = d1.roll() + d2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = d1.num_sides + d2.num_sides
poss_results = range(2, max_result+1)
for roll in poss_results:
    count = results.count(roll)
    frequencies.append(count)

# Display the results.
title = f"Result of rolling two D8s {rolls} times"
labels = {'x': 'Rolls', 'y': 'Frequency of Rolls'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()
