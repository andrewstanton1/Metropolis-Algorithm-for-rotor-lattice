# Metropolis-Algorithm-for-rotor-lattice

- [Metropolis-Algorithm-for-rotor-lattice](#metropolis-algorithm-for-rotor-lattice)
  - [Overview](#overview)
  - [System Requirements](#system-requirements)
  - [Quick Start](#quick-start)
  - [Sample Output](#sample-output)

## Overview

Two programs for sophisticated implementation of a model lattice with nearest neighbor interactions. DFT calculations were performed by collaborator to explore the energetics of F2BODCA-MOF motion of a MOF crystal structure, and the resultant 2-fold symmetry in rotational lattice potential serves as one input to the Hamiltonian used in Monte Carlo simulation. This simulation was used along side experimental probes, including dielectric measurement and solid state NMR, in order to infer about phase transitions and the electronic ground state configuration of this rotor lattice. A visual simulation of the lattice is included in the program files.

## System Requirements

- OS: 64-bit Windows 10
- Processor: Intel Core i3-3210
- Graphics: Intel HD 4000
- RAM: 4 GB
- Disk space: 1 GB

## Quick Start

1. Clone the repo

    ```bash
    $ git clone https://github.com/andrewstanton1/Metropolis-Algorithm-for-rotor-lattice.git
    $ cd Metropolis-Algorithm-for-rotor-lattice/
    ```

1. (Optional) Create and activate a virtual environment

   ```bash
   $ python3 --version
   Python 3.7.0
   $ python3 -m venv env
   $ source env/bin/activate

1. Install the dependencies

    ```bash
    $ pip install -r requirements.txt
    ```

1. Start a Jupyter Notebook server

   ```bash
   $ jupyter notebook
   ```

1. Open a browser and navigate to `http://localhost:8888/notebooks/rotor-model/rotor_model.ipynb`.

1. Click on `Cell > Run All`.

## Sample Output

In the `examples` folder there is an expected output for polarization vs temperature for a run with 10 data points. The `examples` folder also contains snapshots of the state of the lattice are recorded at `N = 1000 * x, x = 0, 1, ..., 10`.  The `rotor_model` notebook should run fairly quickly using the default values in `parameters.py`, but won't produce any meaning results - note: suggested parameters are defined in parameters.py.
