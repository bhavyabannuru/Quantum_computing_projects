from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
qc=QuantumCircuit(1)
print("Enter gates you want to apply on qubit")
gates=input().lower().split()
states=[]
for gate in gates:
    if gate=='x':
      qc.x(0)
    elif gate=='h':
      qc.h(0)
    elif gate == 'y':
      qc.y(0)
    elif gate == 'z':
      qc.z(0) 
    elif gate=='hx':
      qc.h(0)
      qc.x(0)
    elif gate=='t':
      qc.t(0)
    elif gate.startswith('rx'): 
     angle=float(gate[3:-1])
     qc.rx(angle,0)
    elif gate.startswith('ry'):
      angle=float(gate[3:-1])
      qc.ry(angle,0)
    elif gate.startswith('rz'):
      angle=float(gate[3:-1])
      qc.rz(angle,0) 
    else:
      print(f"Invalid gate: {gate}")
    states.append(Statevector.from_instruction(qc)) 
final_state = states[-1]
print("\nFinal Statevector:")
print(final_state)
#  final Bloch sphere plot
plot_bloch_multivector(final_state)
plt.title("Final Bloch Sphere")
plt.show()

#  step-by-step Bloch evolution
for i, state in enumerate(states):
      plot_bloch_multivector(state)
      plt.title(f"After gate {i+1}: {gates[i]}")
      plt.show()
      
qc.draw('mpl')
plt.show()

  

        
 
         




