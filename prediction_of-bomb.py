import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import random
#FLITZUR VAIDMAN APPROACH
def bomb_tester(bomb_present=True):
    qc = QuantumCircuit(1)
    qc.h(0)
    state = Statevector.from_instruction(qc)
    if bomb_present:
        p0 = abs(state.data[0])**2
        p1 = abs(state.data[1])**2
        r = random.random()

        if r < p1:
            return "exploded"
        state = Statevector([1, 0])
    qc = QuantumCircuit(1)
    qc.h(0)
    state = state.evolve(qc)
    p0 = abs(state.data[0])**2
    r = random.random()
    return "D1" if r < p0 else "D2"
def run_trials(N, bomb_present=True):
    results = {"D1": 0, "D2": 0, "exploded": 0}
    for _ in range(N):
        results[bomb_tester(bomb_present)] += 1
    return results
N = 10000
print("Bomb PRESENT:")
print(run_trials(N, True))
print("\nBomb ABSENT:")
print(run_trials(N, False))
