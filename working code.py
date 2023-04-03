import random
import time

class Cont:
    def __init__(self, number, name):
        self.number = number
        self.name = name

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = 4294967311 # A large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
    
    def hash_function(self, key):
        return ((self.a * hash(key) + self.b) % self.p) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # raise KeyError(key)
    
    def print(self):
        l = 0
        k = 0
        for i in self.table:
            if len(i) > k:
                k = len(i)
            # print(l,i)
            l = l+1

        print("longest collision:",k)


# phone_book = [('Alice', '555-1234'), ('Bob', '555-5678'), ('Charlie', '555-9012')]
# phone_book = [('Alice', 5551234), ('Bob', 5555678), ('Charlie', 5559012)]
def randContacts():
    phone_book = []
    for i in range(1000):
        numb = random.randint(0,9999999)
        # a = random.randbytes(3)
        # nam = a.decode('latin-1')
        nam = random.randint(0,999)
        phone_book.append([numb,nam])
        # print(numb, nam)
    phone_book[157] = [12345,343]
    return phone_book

#phone_book = [(5551234, 'Alice'), (5555678, 'Bob'), (5559012, 'dfv'),(3215236, 'vfdfva'),(623541234, 'bafdad'),(14361346, 'bgfsfg'),(64136134, 'bag'),(57714571456, 'vfdahbad'),(3415346, 'vfadv')]
phone_book = randContacts()

ht = Hashtable(len(phone_book))

for name, number in phone_book:
    ht.insert(name, number)

print(ht.get(5551234))
start_time = time.time()
ht.print()
end_time = time.time()
print("Elapsed time:", (end_time - start_time) * 1000, "milliseconds")

start_time = time.time()
print(ht.get(12345))
end_time = time.time()
print("Elapsed time:", (end_time - start_time) * 1000, "milliseconds")

