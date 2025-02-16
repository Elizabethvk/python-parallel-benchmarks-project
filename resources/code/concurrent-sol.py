import time
import numpy as np
import os
import psutil
from statistics import stdev, mean, median
from random import seed
from typing import List, Optional
import concurrent.futures

# Define a computationally intensive function for testing
def matrix_calculation() -> np.ndarray:
    try:
        return np.linalg.inv(np.random.rand(100, 100)) @ np.random.rand(100, 100)
    except np.linalg.LinAlgError:
        print("Matrix inversion failed. Returning an identity matrix.")
        return np.eye(100)

# Function to measure memory usage
def memory_usage() -> float:
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)

def report_statistics(times: List[float]) -> None:
    print("\nResults:")
    print(f"Total Times Recorded: {times}")
    print(f"Longest Time: {max(times):.2f} ms")
    print(f"Fastest Time: {min(times):.2f} ms")
    print(f"Average Time: {mean(times):.2f} ms")
    print(f"Median Time: {median(times):.2f} ms")
    print(f"Standard Deviation: {stdev(times):.2f} ms\n")

def run_task(i: int) -> float:
    start_time = time.time()
    result = matrix_calculation()
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    return elapsed_time

def main_parallel(samples: int = 5, ext_seed: Optional[int] = None) -> None:
    print("Method: Parallel (concurrent.futures)")
    print(f"Performing {samples} runs")
    if ext_seed is not None:
        print(f"Seeding random with {ext_seed}")
        seed(ext_seed)
    print("-" * 40)

    # Parallel execution using ThreadPoolExecutor
    times = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_task, i) for i in range(samples)]
        for future in concurrent.futures.as_completed(futures):
            elapsed_time = future.result()
            print(f"Task completed with Elapsed Time: {elapsed_time:.2f} ms")
            times.append(elapsed_time)

    report_statistics(times)

if __name__ == "__main__":
    samples = int(os.getenv("SAMPLES", 5))
    seed_value = os.getenv("SEED")
    seed_value = int(seed_value, 0) if seed_value else None

    main_parallel(samples=samples, ext_seed=seed_value)
