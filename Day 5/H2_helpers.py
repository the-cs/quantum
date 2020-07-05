import numpy as np
import matplotlib.pyplot as plt
from qiskit import Aer
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import NumPyMinimumEigensolver, VQE
from qiskit.aqua.components.optimizers import SPSA
from qiskit.chemistry.core import Hamiltonian, TransformationType, QubitMappingType
from qiskit.chemistry.drivers import HDF5Driver
import warnings
warnings.filterwarnings('ignore')

def get_H2_Hamiltonian(bond_length):

    operator =  Hamiltonian(transformation=TransformationType.FULL,
                    qubit_mapping=QubitMappingType.PARITY,
                    two_qubit_reduction=True,
                    freeze_core=False,
                    orbital_reduction=None)
            
    if bond_length==0.735: driver= HDF5Driver("H2/H2_equilibrium_0.735_sto-3g.hdf5")
    else: driver= HDF5Driver("H2/{:1.1f}_sto-3g.hdf5".format(bond_length))
    qubit_op, aux_ops = operator.run(driver.run())

    return qubit_op, operator