import cirq
import numpy as np
import matplotlib

#print(cirq.google.Bristlecone)

a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")

ops = [cirq.H(a), cirq.H(b), cirq.CNOT(b,c), cirq.H(b)]

circuit = cirq.Circuit(ops)

print(circuit)
print()
print(cirq.unitary(cirq.H))
print()

for i, moment in enumerate(circuit):
    print("Moment {}: {}".format(i, moment))

print()
print(repr(circuit))

def xor_swap(a, b):
    yield cirq.CNOT(a, b)
    yield cirq.CNOT(b, a)
    yield cirq.CNOT(a, b)

def left_rotate(qubits):
    for i in range(len(qubits) - 1):
        a, b = qubits[i:i+2]
        yield xor_swap(a, b)

line = cirq.LineQubit.range(5)
print(cirq.Circuit(left_rotate(line)))

# InsertStrategy
# EARLIEST
# NEW
# INLINE
# NEW_THEN_INLINE

circuit = cirq.Circuit()
circuit.append([cirq.CZ(a, b)])
circuit.append([cirq.H(a), cirq.H(b), cirq.H(c)])

print()
print(circuit)







