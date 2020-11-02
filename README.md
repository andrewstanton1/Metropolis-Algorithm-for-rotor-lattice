# Metropolis-Algorithm-for-rotor-lattice

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Demo](#demo)
- [Instructions for use](#instruction-for-use)

# Overview
Two programs for sophisticated implementation of a model lattice with nearest neighbor interactions. DFT calcuations were performed by collaborator to explore the energetics of F2BODCA-MOF motion of a MOF crystal structure, and the resultant 2-fold symmetry in rotational lattice potential serves as one input to the Hamiltonian used in Monte Carlo simulation. This simulation was used along side experimental probes, including dielectric measruement and solid state NMR, in order to infer about phase transitions and the electronic ground state configuration of this rotor lattice. A visual simulation of the lattice is included in the program files. 

# System Requirements
## Hardware Requirements
Program requires only a computer with at least 4gb of RAM.

## Software requirements
### OS Requirements
This program is supported for *Windows*. The program has been tested on the following systems:
+ Windows: 10

 ### Python Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependenices. See requirements.txt
```bash
pip install notebook
pip install cython
pip install numpy
pip install matplotlib

-Additionally, install the following for lattice-visual-model for real time visual simulation 
pip install PyQt5
pip install mayavi
```
# Installation Guide:
### Checkout from Github
```
git clone https://github.com/andrewstanton1/Metropolis-Algorithm-for-rotor-lattice.git
```
# Demo:
In the demo folder there is an expected output for polarization vs temperature for a run with 10 data points. The demo folder also contains snapshots of the state of the lattice are recorded at N = 1000*x, x=0,1,...,10. The expected runtime of this demo is 1 hour and 15 minutes on average. 

# Instructions for use:
Launch a Jupyter Notebook session in the rotor-model directory. Run pip install -r requirements.txt  
Configure parameters in parameters.py (note: default parameters are set for demoing). Run each cell in the rotor_model notebook to calculate the polarization across temperature. Run each cell in lattice_visual_random to generate a real-time simulation of the lattice structure.
