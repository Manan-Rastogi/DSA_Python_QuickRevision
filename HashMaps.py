# Hash maps using ASCII

class HashMap:
    def __init__(self):
        self.MAX= 100
        self.arr= [None for i in range(self.MAX)]

    def get_hash(self, key:str):
        '''
        get_hash method accepts a key(string) and returns a hash val based on sum of 
        ASCII of each char and mod by 100
        '''
        h= 0
        for char in key:
            h += ord(char)
        return h % 100                 # assuming 100 size for practice purpose

    # using some magic methods
    def __setitem__(self, key:str, val):
        '''
        this method adds a new key-value pair in the HashMap()
        '''
        # check for len of arr as well.
        h= self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self, key):
        '''
        this method gets the value against the key
        '''
        h= self.get_hash(key)
        return self.arr[h]            # check for len of arr as well.
    
    def __delitem__(self, key):
        h= self.get_hash(key)
        self.arr[h] = None



if __name__ == '__main__':
    t= HashMap()
    
    # print('Hash generated for nov 21 = ', t.get_hash('nov 21'))

    t['nov 22'] = 500
    t['nov 23'] = 200
    t['nov 26'] = 100

    print(t['nov 22'])

    del t['nov 22']

    print(t['nov 22'])
    print(t['nov 23'])

