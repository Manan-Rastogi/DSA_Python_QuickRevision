class HashTable:
    def __init__(self):
        # Initialize the hash table with a specified size (self.MAX)
        self.MAX = 10
        # Create an array of empty lists to store key-value pairs
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        '''
        Calculate the hash value for a given key
        '''
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.MAX

    def __getitem__(self, key):
        '''
        Retrieve the value associated with a given key
        '''
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        '''
        Set the value for a given key
        '''
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                # If the key already exists, update its value
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            # If the key doesn't exist, add a new key-value pair
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        '''
        Delete the key-value pair associated with a given key
        '''
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                # Delete the key-value pair if the key is found
                print("Deleting:", kv)
                del self.arr[arr_index][index]


if __name__ == "__main__":
    # Create an instance of the HashTable class
    my_table = HashTable()

    # Insert key-value pairs
    my_table["apple"] = 5
    my_table["banana"] = 7
    my_table["orange"] = 10
    my_table["elppa"] = 15

    print(my_table.arr)

    # Retrieve values
    print("Value for 'apple':", my_table["apple"])
    print("Value for 'banana':", my_table["banana"])

    # Update values
    my_table["apple"] = 8
    print("Updated value for 'apple':", my_table["apple"])

    # Delete a key-value pair
    del my_table["banana"]
    print("Value for 'banana' after deletion:", my_table["banana"])
