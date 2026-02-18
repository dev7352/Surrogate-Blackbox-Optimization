import numpy as np

def system_runtime(x):
    x1, x2, x3 = x
    
    noise = np.random.normal(0, 0.2)
    
    runtime = (0.5 * (x1 - 2)**2 + np.sin(1.5 * x2) + 0.3 * np.exp(0.5 * x3) + 0.2 * x1 * x3 + noise
    )
    
    return runtime
