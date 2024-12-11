# B31210_MSCS11_Algorithms


#Hybrid data structurs
##It combines the strengths of binary search trees(BSTs) and hash tables to optimize operations like search, insertion, and deletion. Traditional BSTs offer ordered storage and efficient traversal but may degrade to linear time complexity in the worst case. Hash tables provide constant-time average-case operations but lack ordered data access. 


Tests identified to be done:
- dataset1 with integer keys and dataset2 with string keys
- test duplicate keys: if it replaces entries of same key (check if item (15,"len) exists in the tree after insertion dataset1)
- test insertion, deletion, searching, and structure after deletion and insertion
-  test with varying data sizes
- test with integer keys and string keys
- test with sorted dataset
- test collision: keys resolve to the same bucket index 
- test range queries
- test with varrying table size