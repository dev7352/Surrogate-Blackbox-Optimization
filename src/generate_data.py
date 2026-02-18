import numpy as np
import pandas as pd
from system import system_runtime

samples = []

for _ in range(500):
    x = np.random.uniform(0, 5, size=3)
    y = system_runtime(x)
    samples.append([*x, y])

df = pd.DataFrame(samples, columns=["x1", "x2", "x3", "runtime"])
df.to_csv("../data/samples.csv", index=False)

print("Dataset generated.")
