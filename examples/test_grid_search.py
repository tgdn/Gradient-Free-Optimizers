import numpy as np
from gradient_free_optimizers import GridSearchOptimizer

def objective_function(pos_new):
    # (1/3)*x^3 + y^2 + 2*x*y - 6*x - 3*y +4
    x1 = pos_new["x1"]
    x2 = pos_new["x2"]
    score = 1/3 * x1**3 + x2**2 + 2*x1*x2 - 6*x1 - 3*x2 + 4
    return score

search_space = {
    "x1": np.arange(-4, 4, 0.5),
    "x2": np.arange(-2, 4, 0.5),
}

opt = GridSearchOptimizer(search_space)
opt.search(objective_function, n_iter=1000)
