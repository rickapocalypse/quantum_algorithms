from qiskit import *

def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

backend = BasicAer.get_backend('qasm_simulator')

job = execute(qc, backend, shots=1).result()
count = job.get_counts(qc)

print(bit_from_counts(count))