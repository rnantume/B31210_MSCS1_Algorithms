import timeit
import random
from HybridDS import Hybrid_DS  
import sys
sys.setrecursionlimit(2000)  # Increase recursion depth limit

# Function to benchmark an operation
def benchmark_operation(dataset_size, operation_code, setup_code):
    execution_time = timeit.timeit(stmt=operation_code, setup=setup_code, number=100)
    return execution_time

# Generate datasets for different cases
def generate_dataset(size, case):
    if case == "best":
        return list(range(size))  # Sequential data for best-case insertion
    elif case == "worst":
        # Keys are crafted to hash to same buckect (high collisions)
        bucket_index = 0
        # Descending order data for unbalanced BST
        return [bucket_index + size * i for i in range(size, 0, -1)] 
    elif case == "average":
        return random.sample(range(size * 10), size)  # Random data for balanced BST

# Test configurations
dataset_sizes = [10, 100, 1000, 10000]
cases = ["best", "average", "worst"]

# Iterate through cases and dataset sizes
for case in cases:
    print(f"\nTesting {case.capitalize()} Case Performance:")
    for size in dataset_sizes:
        print(f"  Dataset Size: {size}")

        # Generate the dataset
        dataset = generate_dataset(size, case)

        # Setup code for the Hybrid_DS
        setup_code = f"""
from HybridDS import Hybrid_DS
hybrid_ds = Hybrid_DS(100)
dataset = {dataset}
for key in dataset:
    hybrid_ds.insert(key, "value_" + str(key))  # Insert into Hybrid_DS
"""

        # Insertion Benchmark (additional insert)
        insertion_code = f"hybrid_ds.insert({size + 1}, 'value_{size + 1}')"
        insertion_time = benchmark_operation(size, insertion_code, setup_code)
        print(f"    Insertion Time: {insertion_time:.6f} seconds")

        # Search Benchmark (search for a specific key)
        search_key = dataset[size // 2] if case != "best" else 0  # Middle key or root
        search_code = f"hybrid_ds.search({search_key})"
        search_time = benchmark_operation(size, search_code, setup_code)
        print(f"    Search Time: {search_time:.6f} seconds")

        # Deletion Benchmark (delete a specific key)
        deletion_key = dataset[size // 2] if case != "best" else 0  # Middle key or root
        deletion_code = f"hybrid_ds.delete({deletion_key})"
        deletion_time = benchmark_operation(size, deletion_code, setup_code)
        print(f"    Deletion Time: {deletion_time:.6f} seconds")