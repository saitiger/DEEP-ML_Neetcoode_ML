import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]

# Solution 2 : With Permutation

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)
    idx = np.random.permutation(X.shape[0])    
    return X[idx],y[idx]
