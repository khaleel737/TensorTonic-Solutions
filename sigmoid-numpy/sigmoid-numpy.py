import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x, dtype=float)
    # Write code here
    sig = 1 / (1 + np.exp(-x))
    
    return sig