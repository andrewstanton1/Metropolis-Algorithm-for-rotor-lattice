# Metropolis-Algorithm-for-rotor-lattice

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)

# Overview
Two programs for sophisticated implementation of a model lattice with nearest neighbor interactions. DFT calcuations were performed by collaborator to explore the energetics of F2BODCA-MOF motion of a MOF crystal structure, and the resultant 2-fold symmetry in rotational lattice potential serves as one input to the Hamiltonian used in Monte Carlo simulation. This simulation was used along side experimental probes, including dielectric measruement and solid state NMR, in order to infer about phase transitions and the electronic ground state configuration of this rotor lattice. A visual simulation of the lattice is included in the program files. 

# System Requirements
## Hardware Requirements
Program requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
This program is supported for *Windows*. The program has been tested on the following systems:
+ Windows: 10

 ### Python Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependenices. See requirements.txt
```bash
pip install cython
pip install numpy
pip install scipy

-Used in lattice-visual-model for real time visual simulation 
pip install PyQt5
pip install mayavi
pip install vtk
```
# Installation Guide:
### Checkout from Github
```
git clone https://github.com/andrewstanton1/Metropolis-Algorithm-for-rotor-lattice.git
```
