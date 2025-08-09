import matplotlib.pyplot as plt

values = range(1, 5001)
cubes = [x**3 for x in values]

fig, ax = plt.subplots()
ax.scatter(values, cubes, s=10, c=cubes, cmap=plt.cm.Reds)

# Set title and label axes.
ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set tick labels.
ax.tick_params(labelsize=14)

plt.show()
