#Program that utilizes the Hybrid Hash-BST data structure

from HybridDS import BST_Node, Binary_Search_Tree, Hybrid_DS

def main():
    # Initialize the Hybrid_DS with a table size of 6
    hybrid1 = Hybrid_DS(7)

    dataset1= [(10, "bae"), (5, "tim"), (15, "len"), 
              (20, "moe"), (18, "mia"), (25, "zoe"), 
              (15, "sue"), (12, "lou"), (18, "rae")] 

    dataset2 = [("bae", "Kenya"), ("tim", "Uganda"), ("len", "Tanzania"),
                 ("moe", "Rwanda"), ("mia", "DRC"), ("zoe", "S.Sudan"), 
                 ("sue", "Egypt"), ("lou", "Uganda"), ("rae", "Kenya")]

    print("Inserting data from dataset1:")
    for key, value in dataset1:
        hybrid1.insert(key, value)
        print(f"Inserted ({key}, {value})")

    print("\nPrinting items in hybrid1 after insertion:")
    hybrid1.display_items()
    
    print("\nSearching for keys in dataset1:")
    search_keys = [15, 20, 50]  # keys may exist or not
    #search_keys2 = ["bae", "rob", "mia"]
    for key in search_keys:
        result = hybrid1.search(key)
        if result:
            print(f"Key {key} found with value: {result}")
        else:
            print(f"Key {key} not found.")

    print("\nDeleting keys from dataset1:")
    delete_keys = [20, 35, 50]  # keys may exist or not
    #delete_keys2 = ["bae", "rob", "mia"]
    for key in delete_keys:
        success = hybrid1.delete(key)
        if success:
            print(f"Key {key} deleted successfully.")
        else:
            print(f"Key {key} not found for deletion.")

    print("\nSearching again after deletions:")
    for key in search_keys:
        result = hybrid1.search(key)
        if result:
            print(f"Key {key} found with value: {result}")
        else:
            print(f"Key {key} not found.")

    print("\nPrinting items in hybrid1 after deletion:")
    hybrid1.display_items()

if __name__ == "__main__":
    main()


#deletion of non existing string keys
#ways to view data after operations