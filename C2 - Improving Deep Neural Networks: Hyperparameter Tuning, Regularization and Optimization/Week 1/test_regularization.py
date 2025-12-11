import numpy as np

keep_prob = 0.7

d3 = np.random.rand(1, 10)

d3 = np.round(d3, 2)

print(d3)

d3 = d3 < keep_prob

print(np.sum(d3))
