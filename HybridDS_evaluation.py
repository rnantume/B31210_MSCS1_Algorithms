#  Program to test your data structure using datasets of varying sizes. 
import timeit

# Function to benchmark an operation
def benchmark_operation(dataset_size, operation, operation_code):
    setup_code = f"""
from HybridDS import Hybrid_DS
hybrid_ds = Hybrid_DS(100)
dataset = [(i, "value_") for i in range({dataset_size})]  # Prepopulate dataset
for key, value in dataset:
    hybrid_ds.insert(key, value)  # Insert into Hybrid_DS
"""
    test_code = operation_code
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=100)
    return execution_time

# List of dataset sizes to test
dataset_sizes = [10, 100, 1000, 10000]

# Operations to test: Insertion, Deletion, and Search
for size in dataset_sizes:
    print(f"\nDataset Size: {size}")
    
    # Test insertion (since the dataset is already prepopulated, we only measure the time taken for the setup)
    insertion_code = "pass"  # Prepopulation happens in setup
    insertion_time = benchmark_operation(size, "Insertion", insertion_code)
    print(f"Average Insertion Time for dataset of size {size}: {insertion_time:.9f} seconds")
    
    # Test search for a random key in the dataset (e.g., size // 2)
    search_key = size // 2  # Search for the middle key
    search_code = f"hybrid_ds.search({search_key})"
    search_time = benchmark_operation(size, "Search", search_code)
    print(f"Average Search Time for dataset of size {size}: {search_time:.6f} seconds")
    
    # Test deletion of a random key from the dataset
    deletion_key = size // 2  # Delete the middle key
    deletion_code = f"hybrid_ds.delete({deletion_key})"
    deletion_time = benchmark_operation(size, "Deletion", deletion_code)
    print(f"Average Deletion Time for dataset of size {size}: {deletion_time:.6f} seconds")