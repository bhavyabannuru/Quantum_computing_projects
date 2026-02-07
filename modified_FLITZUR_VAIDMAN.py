from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
from qiskit import transpile
import numpy as np

# -------------------------
# Parameters
# -------------------------
N = 20
theta = np.pi/(2*N)
shots = 5000

sim = AerSimulator()

# =====================================================
# 🧯 Dud bomb — rotations accumulate (no mid measurement)
# =====================================================
qc_dud = QuantumCircuit(1, 1)

for _ in range(N):
    qc_dud.ry(2*theta, 0)   # R_y uses half-angle convention

qc_dud.measure(0, 0)

tqc = transpile(qc_dud, sim)
result = sim.run(tqc, shots=shots).result()
print("\nDUD bomb counts:")
print(result.get_counts())


# =====================================================
# 💣 Working bomb — measure each step (Zeno effect)
# =====================================================
q = QuantumRegister(1)
c = ClassicalRegister(N + 1)   # store each step result
qc_work = QuantumCircuit(q, c)

for i in range(N):
    qc_work.ry(2*theta, 0)

    # bomb check measurement
    qc_work.measure(0, c[i])

    # if safe (measured 0) → reset to |0>
    qc_work.reset(0)

# final test rotation attempt
qc_work.measure(0, c[N])

tqc2 = transpile(qc_work, sim)
result2 = sim.run(tqc2, shots=shots).result()
counts2 = result2.get_counts()

print("\nWORKING bomb counts (bitstrings show step outcomes):")
print(counts2)
