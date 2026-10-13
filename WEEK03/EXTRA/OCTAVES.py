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

WIDTH, HEIGHT = 500, 500
scale = 0.005
heightmap = np.zeros((HEIGHT, WIDTH))
for i in range(HEIGHT):
    for j in range(WIDTH):
        heightmap[i, j] = fbm(j * scale, i * scale)
heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())

terrain = np.zeros((HEIGHT, WIDTH, 3))
for i in range(HEIGHT):
    for j in range(WIDTH):
        h = heightmap[i, j]
        if h < 0.3:
            terrain[i, j] = [0.9, 0.5, 0.4]
        elif h < 0.4:
            terrain[i, j] = [0.8, 0.2, 0.9]
        elif h < 0.5:
            terrain[i, j] = [0.9, 0.8, 0.5]
        elif h < 0.7:
            terrain[i, j] = [0.0, 0.9, 0.5]
        elif h < 0.85:
            terrain[i, j] = [0.4, 0.3, 0.2]
        else:
            terrain[i,j] = [0.9, 0.9, 0.9]

plt.imshow(terrain)
plt.axis('off')
plt.show()