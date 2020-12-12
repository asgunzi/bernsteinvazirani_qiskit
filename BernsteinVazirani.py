# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 04:01:23 2020

@author: asgun
"""


from qiskit import *

qIn = QuantumRegister(3)
qKick =QuantumRegister(1)
cOut = ClassicalRegister(3) 

qc = QuantumCircuit(qIn, qKick,cOut)

qc.h(qIn)
qc.x(qKick)
qc.h(qKick)

qc.barrier()

#Oráculo. Codifica 101
qc.cx(qIn[0],qKick)
qc.cx(qIn[2],qKick)


qc.barrier()

qc.h(qIn)

qc.measure(qIn,cOut)

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=100)
#job = execute(qc, backend=backend, shots=8192)
result = job.result()
count =result.get_counts()

print(count)

print(qc)