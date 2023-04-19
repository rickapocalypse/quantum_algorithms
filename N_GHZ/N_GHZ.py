from qiskit import *
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt

def n_GHZ(qbit):
    qc = QuantumCircuit(qbit,qbit)
    qc.h(0)
    measures = [0]
    for i in range(1,qbit):
        qc.cx(i-1,i)
        measures.append(i)
    qc.barrier()
    qc.measure(measures, measures)
    return qc
