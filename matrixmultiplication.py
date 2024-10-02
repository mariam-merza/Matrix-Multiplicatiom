# Matrix Multiplication Program
# This program multiplies two matrices of size 'size' entered by the user.
# The matrices are initialized with random values ranging from 1 to 100.
# For part 1, as the size of the matrices increase, the time needed for the computation per element increases as well. This is due to the fact that the time complexity of
# matrix multiplication is O(n^3), where n is the size of the matrices. As the size of the matrices increase, the number of operations required to multiply the matrices
# increases, and thus, the runtime increases.
# This can be observed by increasing the matrix size in the code and observing the elapsed time, number of elements in the result matrix, and time per element.
# For Part 1, the code was run without profiling, and the runtimes were only impacted by the code itself. The time needed for the computation increased as the size of
# the matrices increased. This is because the multiplication operation involves three nested for loops that have to be executed for each element in the matrices.
# For Part 2, profiling was enabled, and the runtimes were different from Part 1. This is because the profiler adds some overhead to the code, which affects its
# performance. The memory requirements of the code were also displayed, providing insights into how the code is using memory.

import time
from memory_profiler import profile # type: ignore

@profile
def multiply(A, B):
    size = len(A)
    P = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                P[i][j] += A[i][k] * B[k][j]  # multiplication
    return P

def get_matrix(size, name):
    matrix = []
    for i in range(size):
        row = input(f"Enter row {i+1} of {name} (space-separated values): ")
        matrix.append(list(map(int, row.split())))
    return matrix

size = int(input("Enter size: "))

A = get_matrix(size, "A")
B = get_matrix(size, "B")

start_time = time.time()  # code to start timer
P = multiply(A, B)
elapsed_time = time.time() - start_time  # code to stop timer

num_elements = size * size * 3  # number of elements in matrices A, B and P
time_per_element = elapsed_time / num_elements * 1000

print("Elapsed time: ", elapsed_time, " seconds")
print("Number of elements in result matrix: ", num_elements)
print("Time per element: ", time_per_element, " ms")
print("Result matrix:")
for row in P:
    print(" ".join(str(x) for x in row))