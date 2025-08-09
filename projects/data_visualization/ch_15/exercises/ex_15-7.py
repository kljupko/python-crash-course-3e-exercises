import plotly.express as px

from die import Die

# Create three D6s.
d1, d2, d3 = Die(), Die(), Die()

# Generate rolls.
results = []
rolls = 1_000_000
for _ in range(rolls):
    result = d1.roll() + d2.roll() + d3.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = d1.num_sides * 3
poss_results = range(3, max_result+1)
for roll in poss_results:
    count = results.count(roll)
    frequencies.append(count)

# Display the results.
title = f"Result of rolling three D6s {rolls} times"
labels = {'x': 'Rolls', 'y': 'Frequency of Rolls'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()
