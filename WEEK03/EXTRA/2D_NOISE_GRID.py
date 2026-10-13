import numpy as np
import opensimplex 
import matplotlib.pyplot as plt


WIDTH, HEIGHT = 100, 100
scale = 0.05
noise_grid = np.zeros((HEIGHT, WIDTH))
for i in range(HEIGHT):
    for j in range(WIDTH):
        noise_grid[i, j] = (opensimplex.noise2(j * scale, i * scale) + 1) / 2
plt.imshow(noise_grid, cmap='gray')
plt.colorbar()
plt.show()