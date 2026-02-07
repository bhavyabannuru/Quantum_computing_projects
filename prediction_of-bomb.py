from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

N = int(input("enter no.of times you want to run the loop: "))
theta = np.pi/(2*N)
shots = 5000
sim = AerSimulator()

# DUD bomb
qc_dud = QuantumCircuit(1, 1)
for _ in range(N):
    qc_dud.ry(2*theta, 0)

qc_dud.measure(0, 0)

tqc = transpile(qc_dud, sim)
result_dud = sim.run(tqc, shots=shots).result()

print("\nDUD bomb counts:")
print(result_dud.get_counts())


# WORKING bomb
qc_work = QuantumCircuit(1, 1)
for _ in range(N):
    qc_work.ry(2*theta, 0)
    qc_work.measure(0, 0)
    qc_work.reset(0)

qc_work.measure(0, 0)

tqcw = transpile(qc_work, sim)
result_work = sim.run(tqcw, shots=shots).result()

print("\nWORKING bomb counts:")
print(result_work.get_counts())
