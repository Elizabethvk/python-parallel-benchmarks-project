import time
import numpy as np
import os
import psutil
from statistics import stdev, mean, median
from random import random, seed
from typing import List, Optional

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

def main(samples: int = 5, ext_seed: Optional[int] = None) -> None:
    print("Method: Sequential")
    print(f"Performing {samples} runs")
    if ext_seed is not None:
        print(f"Seeding random with {ext_seed}")
        seed(ext_seed)
    print("-" * 40)

    times = []

    for i in range(samples):
        print(f"\nStarting iteration {i + 1}/{samples}")
        start_time = time.time()
        start_memory = memory_usage()

        result = matrix_calculation()

        end_time = time.time()
        end_memory = memory_usage()

        elapsed_time = (end_time - start_time) * 1000
        memory_diff = end_memory - start_memory

        print(f"Iteration {i + 1} completed")
        print(f"Elapsed Time: {elapsed_time:.2f} ms")
        print(f"Memory Usage Difference: {memory_diff:.4f} MB")
        print("-" * 40)

        times.append(elapsed_time)

    report_statistics(times)

if __name__ == "__main__":
    samples = int(os.getenv("SAMPLES", 5))
    seed_value = os.getenv("SEED")
    seed_value = int(seed_value, 0) if seed_value else None

    main(samples=samples, ext_seed=seed_value)
