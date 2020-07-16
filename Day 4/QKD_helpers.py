import binascii
from qutip import *
from qiskit import execute, Aer, IBMQ, QuantumCircuit

def mystery_state_circuit():
	qc = QuantumCircuit(1,1)
	qc.x(0)
	qc.h(0)
	return qc

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def generate_secret_key():
    return text_to_bits('hello quantum world!')