import time
import numpy as np
from numba import jit, prange

# JIT-compiled function for matrix calculation
@jit(nopython=True, parallel=True)
def matrix_calculation_parallel():
    A = np.random.rand(100, 100)
    B = np.random.rand(100, 100)
    result = np.dot(np.linalg.inv(A), B)
    return result

def time_execution(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return (end_time - start_time) * 1000

def main(samples=5):
    print("Method: Parallel with Numba JIT")
    print(f"Performing {samples} runs")
    print("-" * 40)

    times = []
    for i in range(samples):
        print(f"Starting iteration {i + 1}/{samples}")
        elapsed_time = time_execution(matrix_calculation_parallel)
        print(f"Elapsed Time: {elapsed_time:.2f} ms")
        times.append(elapsed_time)
        print("-" * 40)

    print("\nResults:")
    print(f"Longest Time: {max(times):.2f} ms")
    print(f"Fastest Time: {min(times):.2f} ms")
    print(f"Average Time: {sum(times) / len(times):.2f} ms")
    print(f"Standard Deviation: {np.std(times):.2f} ms")

if __name__ == "__main__":
    main(samples=5)
