## Installation

Required libraries for Ubuntu 16.04.

```
sudo apt-get install libopenmpi-dev
sudo apt install openmpi-bin
```

Install [MPI4py](https://pypi.python.org/pypi/mpi4py) and any other dependency

```
pip install -r requirements
```

Install this on each decive in your cluster.

## Run

Execute the script with `mpiexec`. 

```
mpiexec -n 2 --host ip-or-hostname-1,ip-or-hostname-2 python script-name.py

# Example
# mpiexec -n 2 --host 192.168.0.9,192.168.0.7 python first.py
```