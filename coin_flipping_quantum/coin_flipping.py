from qiskit import *

qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1).result()
count = job.data(qc)

print()

if count['counts'].get('0x0') == True:
    print('Colapsou em 0')
else:
    print('Colapsou em 1')