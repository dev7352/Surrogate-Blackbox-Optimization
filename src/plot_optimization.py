import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from system import system_runtime

# Load dataset
df = pd.read_csv("../data/samples.csv")

X = df[["x1", "x2", "x3"]]
y = df["runtime"]

# Train surrogate
model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

# -----------------------------
# Baseline Random Search
# -----------------------------
baseline_best = []
best = float("inf")

for _ in range(200):
    x = np.random.uniform(0, 5, size=3)
    true_y = system_runtime(x)
    best = min(best, true_y)
    baseline_best.append(best)

# -----------------------------
# Surrogate-Guided Search
# -----------------------------
surrogate_best = []
best = float("inf")

for _ in range(200):
    x = np.random.uniform(0, 5, size=3)
    pred = model.predict([x])[0]
    
    if pred < best:
        true_y = system_runtime(x)
        best = min(best, true_y)
    
    surrogate_best.append(best)

# -----------------------------
# Plot
# -----------------------------
plt.plot(baseline_best, label="Baseline Random Search")
plt.plot(surrogate_best, label="Surrogate-Guided Search")

plt.xlabel("Iterations")
plt.ylabel("Best Runtime Found")
plt.title("Optimization Behaviour Comparison")

plt.legend()
plt.savefig("../results/plots/optimization_comparison.png", dpi=300, bbox_inches="tight")
plt.close()

