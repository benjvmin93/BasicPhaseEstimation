import qsharp
from PhaseEstimation import run
import matplotlib.pyplot as plt

n_shots = 0
phi = 0
n_oracle = 1

results_shots = []

for n_shots in range(1, 101):
    result = run.simulate(nShots=n_shots, phi=phi, oraclePower=n_oracle)
    results_shots.append(result)

plt.plot(list(range(1, 101)), results_shots)