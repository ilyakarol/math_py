# sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

import math
from scipy.optimize import minimize, differential_evolution
%matplotlib inline

def function_instanse(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)

# BGFS algorithm
minimize(function_instanse, 2, method='BFGS') # local min
minimize(function_instanse, 30, method='BFGS') # global min

# Differential evolution
differential_evolution(function_instanse, [(1, 30)]) # global min
