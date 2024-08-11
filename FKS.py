import random
import sys
import hashlib

class PerfectHash:
    def __init__(self, keys):
        self.n = len(keys)
        self.m = self.n ** 2  # size of the hash table
        self.keys = keys
        self.primary_hash_table = [None] * self.n
        self.secondary_hash_tables = []
        self.primary_hash_functions = []
        self.secondary_hash_functions = []

        # Find a good primary hash function
        self._find_primary_hash_function()
        # Create secondary hash tables for each bucket
        self._create_secondary_hash_tables()

    def _find_primary_hash_function(self):
        while True:
            self.primary_hash_functions = [self._random_hash_function(self.n) for _ in range(2)]
            collision = False
            buckets = [[] for _ in range(self.n)]
            
            for key in self.keys:
                h1 = self._hash(key, self.primary_hash_functions[0], self.n)
                h2 = self._hash(key, self.primary_hash_functions[1], self.n)
                index = (h1 + h2) % self.n
                buckets[index].append(key)
                if len(buckets[index]) > 1:
                    collision = True
                    break

            if not collision:
                self.primary_hash_table = buckets
                break

    def _create_secondary_hash_tables(self):
        for bucket in self.primary_hash_table:
            if len(bucket) == 0:
                self.secondary_hash_tables.append(None)
                self.secondary_hash_functions.append(None)
            elif len(bucket) == 1:
                self.secondary_hash_tables.append(bucket)
                self.secondary_hash_functions.append([self._random_hash_function(1)])
            else:
                while True:
                    secondary_table_size = len(bucket) ** 2
                    secondary_table = [None] * secondary_table_size
                    secondary_hash_function = self._random_hash_function(secondary_table_size)
                    collision = False
                    
                    for key in bucket:
                        index = self._hash(key, secondary_hash_function, secondary_table_size)
                        if secondary_table[index] is not None:
                            collision = True
                            break
                        secondary_table[index] = key
                    
                    if not collision:
                        self.secondary_hash_tables.append(secondary_table)
                        self.secondary_hash_functions.append(secondary_hash_function)
                        break

    def _random_hash_function(self, modulus):
        a = random.randint(1, sys.maxsize)
        b = random.randint(0, sys.maxsize)
        return lambda x: (a * x + b) % modulus

    def _hash(self, key, hash_function, modulus):
        key_as_int = int(hashlib.md5(key.encode()).hexdigest(), 16)
        return hash_function(key_as_int) % modulus

    def find(self, key):
        h1 = self._hash(key, self.primary_hash_functions[0], self.n)
        h2 = self._hash(key, self.primary_hash_functions[1], self.n)
        primary_index = (h1 + h2) % self.n

        if self.primary_hash_table[primary_index] is None:
            return None

        if len(self.primary_hash_table[primary_index]) == 1:
            return self.primary_hash_table[primary_index][0]

        secondary_table = self.secondary_hash_tables[primary_index]
        secondary_hash_function = self.secondary_hash_functions[primary_index]
        secondary_index = self._hash(key, secondary_hash_function, len(secondary_table))

        return secondary_table[secondary_index]

# 测试
keys = ['apple', 'banana', 'orange', 'grape', 'mango', 'lemon']
fks = PerfectHash(keys)

for key in keys:
    print(f'Key: {key}, Found: {fks.find(key)}')
