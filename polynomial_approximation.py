# sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
%matplotlib inline

def function_instanse(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)

sample_range = np.arange(0, 15, 0.1)

plt.plot(sample_range, map(function_instanse, sample_range), label='instance function')

# 1-polynomial approx
sample_array_1 = [1, 15]
A1 =  map(lambda e: [1, e], sample_array_1)
plt.plot(sample_array_1, sc.linalg.solve([[1, 1],[1, 15]], map(function_instanse, sample_array_1)))

# 2-polynomial approx
sample_array_2 = [1, 8, 15]
A2 = map(lambda e: [1, e, e ** 2], sample_array_2)
plt.plot(sample_array_2, sc.linalg.solve(A2, map(function_instanse, sample_array_2)))

# 3-polynomial approx
sample_array_3 = [1, 4, 10, 15]
A3 = map(lambda e: [1, e, e ** 2, e ** 3], sample_array_3)
plt.plot(sample_array_3, sc.linalg.solve(A3, map(function_instanse, sample_array_3)))
sc.linalg.solve(A3, map(function_instanse, sample_array_3))
