from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
import numpy as np
N = int(input("enter no.of times you want to run the loop: "))
theta = np.pi/(2*N)
shots = 5
q = QuantumRegister(1)
c = ClassicalRegister(N + 1)
qc = QuantumCircuit(q, c)
for i in range(N):
    qc.ry(2*theta, 0)
    qc.measure(0, c[i])
    qc.reset(0)

qc.measure(0, c[N])
sim = AerSimulator()
tqc = transpile(qc, sim)
result = sim.run(tqc, shots=shots).result()
print(result.get_counts())
