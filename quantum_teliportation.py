from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt
qc = QuantumCircuit(3, 2)
qc.ry(np.pi/3, 0)
qc.h(1)
qc.cx(1, 2)
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)
with qc.if_test((1, 1)):
    qc.x(2)
with qc.if_test((0, 1)):
    qc.z(2)
qc.draw("mpl")
plt.show()
