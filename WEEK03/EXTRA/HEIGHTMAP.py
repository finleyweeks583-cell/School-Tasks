import numpy as np
import opensimplex 
import matplotlib.pyplot as plt


WIDTH, HEIGHT = 100, 100
scale = 0.005
heightmap = np.zeros((HEIGHT, WIDTH))
for i in range(HEIGHT):
    for j in range(WIDTH):
        heightmap[i, j] = fbm(j * scale, i * scale)
plt.imshow(heightmap, cmap='gray')
plt.show()