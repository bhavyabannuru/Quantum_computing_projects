from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
#3 qubits,2 classical bits
qc = QuantumCircuit(3)
qc.h(0)        
qc.h(1)
qc.cx(1, 2)
#Alice's operations
qc.cx(0, 1)
qc.h(0)
# Measure Alice's qubits
qc.cx(1, 2)
qc.cz(0, 2)
qc.draw("mpl")
plt.show()
state = Statevector.from_instruction(qc)
print("\nFinal Statevector:\n", state)
