from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
qc = QuantumCircuit(2)
#Base Bell state (Phi+)
qc.h(0)
qc.cx(0, 1)
bell_type = input("Enter bell state (phi_plus / phi_minus / psi_plus / psi_minus): ")
#Bell states
if bell_type == "phi_minus":
    qc.z(0)
elif bell_type == "psi_plus":
    qc.x(1)
elif bell_type == "psi_minus":
    qc.x(1)
    qc.z(0)
elif bell_type == "phi_plus":
    pass  
else:
    print("Invalid Bell state name")
    exit()
#Draw circuit
qc.draw('mpl')
plt.title("Bell State Circuit")
plt.show()
state = Statevector.from_instruction(qc)
# Plot Bloch vector
plot_bloch_vector(state)
plt.title("Bloch Sphere of Qubit 0 (Entangled)")
plt.show()



