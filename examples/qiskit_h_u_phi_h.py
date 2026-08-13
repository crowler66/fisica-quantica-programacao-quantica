from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# Fase usada no experimento
phi = np.pi / 2

# Circuito de um qubit:
# |0> -> H -> RZ(phi) -> H
qc = QuantumCircuit(1)

qc.h(0)
qc.rz(phi, 0)
qc.h(0)

print("Circuito:")
print(qc)

state = Statevector.from_instruction(qc)

print("\nEstado final:")
print(state)

print("\nProbabilidades:")
print(state.probabilities())
