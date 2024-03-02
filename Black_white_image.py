import numpy as np
import matplotlib.pyplot as plt

ar = np.array([[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])

# Plot the array with each grid cell as a pixel
plt.imshow(ar, cmap="gray", extent=[0, 11, 0, 9])

# Define grid with axis='both' to display grid lines on both x and y axes
plt.grid(True, which='both', color='black', linewidth=1)

# Show the tick count on both x and y axes
plt.xticks(np.arange(0,12, 1))
plt.yticks(np.arange(0,10, 1))
plt.savefig("gray-heart")

plt.show()
print(ar.shape)
