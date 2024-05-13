import matplotlib.pyplot as plt

from algos.hash import count_collisions


sizes = [100, 1000, 5000, 10000, 50000, 75000, 100000]
collisions = []

for size in sizes:
    col = count_collisions(size)
    collisions.append(col)

plt.plot(sizes, collisions, label="Collisions")
plt.xlabel("Array Size")
plt.ylabel("Collisions")
plt.legend()
plt.savefig("test.png")
plt.show()
