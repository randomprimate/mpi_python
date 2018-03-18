from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

"""
Transfer dictionary from one node to another
"""

if rank == 0:
 data = {'a': 7, 'b': 3.14}
 comm.send(data, dest=1, tag=11)
 print('from rank 0: ')
 print(data)
else:
 data = comm.recv(source=0, tag=11)
 print('from '+str(rank)+': ')
 print(data)

