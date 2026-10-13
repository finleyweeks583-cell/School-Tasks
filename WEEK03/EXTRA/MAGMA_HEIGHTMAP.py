import numpy as np
import opensimplex 
import matplotlib.pyplot as plt

def fbm(x, y, octaves = 4, persistence=0.5, lacunarity=2.0):
    value = 0.0
    amplitude = 1.0
    frequency = 1.0
    for _ in range(octaves):
        value += opensimplex.noise2(x * frequency, y * frequency) * amplitude
        amplitude *= persistence
        frequency *= lacunarity
    return value

WIDTH, HEIGHT = 100, 100
scale = 0.005
heightmap = np.zeros((HEIGHT, WIDTH))
for i in range(HEIGHT):
    for j in range(WIDTH):
        heightmap[i, j] = fbm(j * scale, i * scale)
heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
plt.imshow(heightmap, cmap='magma')
plt.show()