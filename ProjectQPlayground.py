#http://dataespresso.com/en/2018/07/22/Tutorial-Generating-random-numbers-with-a-quantum-computer-Python/#comments
# ----------------
# Create a quantum random generator
# ----------------
# Import libraries
from projectq.ops import H, Measure
from projectq import MainEngine
# ----------------
# initialize backend
quantum_engine = MainEngine()
# create a new qubit
qubit = quantum_engine.allocate_qubit()

# apply Hadamard gate to Qubit (toss coin in air)
# applying gate directly to qubit because not physically
# possible to copy a qubit
H | qubit

# measure qubit
Measure | qubit

print(int(qubit))
# ----------------
