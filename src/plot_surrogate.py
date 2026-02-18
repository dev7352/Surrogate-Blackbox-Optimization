import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("../data/samples.csv")

X = df[["x1", "x2", "x3"]]
y = df["runtime"]

model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

pred = model.predict(X)

plt.scatter(y, pred, alpha=0.5)
plt.xlabel("True Runtime")
plt.ylabel("Predicted Runtime")
plt.title("Surrogate Model Predictions vs True Runtime")
plt.plot([y.min(), y.max()], [y.min(), y.max()])
plt.savefig("../results/plots/surrogate_predictions.png", dpi=300,bbox_inches="tight")
plt.close()

