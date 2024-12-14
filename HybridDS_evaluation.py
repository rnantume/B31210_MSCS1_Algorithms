#  Program to test your data structure using datasets of varying sizes. 
import timeit

# Defining the setup and the code to test
setup_code = """
from HybridDS import Hybrid_DS, Binary_Search_Tree, BST_Node
hybrid_ds = Hybrid_DS(5)
dataset = [(i, f"value_{i}") for i in range(10)]
for key, value in dataset:
    hybrid_ds.insert(key, value)  # Inserting data in the data structure
"""

test_code = """
hybrid_ds.search(5)  # Test searching for an existing key
"""

# Run the timeit benchmark
execution_time = timeit.timeit(test_code, setup=setup_code, number=10)  # Repeat the test 10 times
print(f"Average time for 10 search operations: {execution_time:.6f} seconds")