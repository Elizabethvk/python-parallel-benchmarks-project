# Benchmarking Python Parallelization: Joblib, Multiprocessing, Concurrent Futures, and Numba
## python-parallel-benchmarks-project

## Parallelization Benchmarking Project

This project benchmarks and compares different parallelization approaches in Python for computationally intensive tasks. It provides a flexible framework to test and analyze the performance of **Joblib**, **Multiprocessing**, **Numba**, and **Concurrent.futures** on CPU-bound tasks.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Methods Tested](#methods-tested)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

Parallelization is a powerful technique to speed up computations by distributing tasks across multiple CPU cores or threads. This project evaluates the performance of four popular Python parallelization libraries:
- **Joblib**: Simple and memory-efficient parallelization.
- **Multiprocessing**: Low-level multiprocessing for CPU-bound tasks.
- **Numba**: Just-In-Time (JIT) compilation with parallel loop execution.
- **Concurrent.futures**: High-level interface for threading and multiprocessing.

The project includes:
- A **test function** to benchmark each method.
- **Memory and timing measurements** to evaluate performance.
- A **flexible framework** to test custom functions and iterables.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/parallelization-benchmark.git
   cd parallelization-benchmark
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   ```
   numpy
   joblib
   numba
   psutil
   ```

---

## Usage

### Running the Benchmark

To run the benchmark, execute the following command:
```bash
python test_parallelization.py
```

This will test all four parallelization methods (`joblib`, `multiprocessing`, `numba`, and `concurrent_futures`) on a sample CPU-bound task (matrix multiplication).

### Customizing the Test

You can customize the test by modifying the following parameters in the `test_parallelization.py` script:

1. **Task Function**:
   Replace the `fun(x)` function with your own computationally intensive task:
   ```python
   def fun(x):
       # Your custom task here
       return result
   ```

2. **Iterable Size**:
   Adjust the size of the iterable to test scalability:
   ```python
   iterable = range(100)  # Change 100 to your desired size
   ```

3. **Number of Workers**:
   Set the number of workers/threads/processes:
   ```python
   num_workers = 8  # Adjust based on your CPU cores
   ```

4. **Numba Optimization**:
   If using Numba, ensure your function is compatible with `@njit(parallel=True)`.

---

## Methods Tested

### 1. **Joblib**
- **Description**: Joblib provides a simple interface for parallelizing loops using multiprocessing or threading.
- **Strengths**: Easy to use, memory-efficient, and supports lazy evaluation.
- **Weaknesses**: Higher overhead for small tasks.

### 2. **Multiprocessing**
- **Description**: The `multiprocessing` module uses separate processes to bypass the Global Interpreter Lock (GIL).
- **Strengths**: Highly efficient for CPU-bound tasks.
- **Weaknesses**: High memory usage due to separate processes.

### 3. **Numba**
- **Description**: Numba uses JIT compilation to optimize numerical computations and supports parallel loops with `prange`.
- **Strengths**: Extremely fast for numerical tasks.
- **Weaknesses**: Limited to specific Python features and requires compilation.

### 4. **Concurrent.futures**
- **Description**: Provides a high-level interface for threading (`ThreadPoolExecutor`) and multiprocessing (`ProcessPoolExecutor`).
- **Strengths**: Flexible and easy to use.
- **Weaknesses**: Higher overhead compared to lower-level libraries.

---

## Results

The benchmark will output the time taken and memory usage for each method. Example output:

```
Method: joblib
Time taken: 12.3456 seconds
Memory usage: 123.4567 MB
----------------------------------------
Method: multiprocessing
Time taken: 10.2345 seconds
Memory usage: 234.5678 MB
----------------------------------------
Method: numba
Time taken: 8.1234 seconds
Memory usage: 50.1234 MB
----------------------------------------
Method: concurrent_futures
Time taken: 11.5678 seconds
Memory usage: 200.1234 MB
----------------------------------------
```

### Key Metrics
- **Time Taken**: Measures the execution time of each method.
- **Memory Usage**: Tracks the memory consumption during execution.
