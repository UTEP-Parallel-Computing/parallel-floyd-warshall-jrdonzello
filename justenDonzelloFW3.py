from mpi4py import MPI
import time
comm = MPI.COMM_WORLD
matrix = [[0,999999,999999,31,85,56,999999,40,32,9999999],
           [31, 0, 999999, 30, 999999, 32, 56, 999999, 20, 999999],
           [999999, 999999, 0, 999999, 999999, 999999, 999999, 30, 999999, 73],
           [87, 42, 58, 0, 999999, 999999, 999999, 999999, 999999, 999999],
           [23, 999999, 35, 93, 0, 999999, 999999, 999999, 29, 999999],
           [70, 95, 17, 999999, 86, 0, 91, 999999, 89, 999999],
           [999999, 999999, 999999, 80, 48, 999999, 0, 999999, 999999, 30 ],
           [999999, 999999, 55, 26, 87, 999999, 18, 0, 17, 50]]
rowsPerThr = len(matrix) / comm.Get_size()
startRow = rowsPerThr * comm.Get_rank()
endRow = rowsPerThr * (comm.Get_rank() + 1)
threadsPerRow = comm.Get_size() / len(matrix)
#print(rowsPerThr)
#print('{} {} '.format(int(startRow), int(endRow)))
#print(comm.Get_rank())
start = time.monotonic()
for i in range(len(matrix)):
    owner = int(threadsPerRow * i)
    #print(owner)
    matrix[i] = comm.bcast(matrix[i], root=owner)
    for j in range(int(startRow), int(endRow)):
        for k in range(len(matrix)):
            matrix[j][k] = min(matrix[j][k], matrix[j][i]+matrix[i][k])
#print(matrix)
if comm.Get_rank() == 0:
    for x in range(int(endRow), len(matrix)):
        owner = int(threadsPerRow * x)
        matrix[x] = comm.recv(source=owner, tag=x)
else:
    for x in range(int(startRow), int(endRow)):
        comm.send(matrix[x], dest=0, tag=x)
end = time.monotonic() - start
print(matrix)
print(end)
