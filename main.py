# python3
import random

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class Cont:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def get_prime(i):
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    n = i+1
    while True:
        if is_prime(n):
            return n
        n = n+1

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    # declare hash table with size
    size = 0
    for cur_query in queries:
        if cur_query.type == 'add':
            size = size + 1
    
    # declare emply hash table
    hash_table = [[] for i in range(size)]
    
    # nitialising hash function variables
    p = get_prime(size)
    a = random.randint(1, p-1)
    b = random.randint(0, p-1)

    # declaring hash function
    def hash_function(number):
        return ((a * hash(number) + b) % p) % size
    
    result = []

    for cur_query in queries:
        if cur_query.type == 'add':
            hashed_index = hash_function(cur_query.number)
            for i in hash_table[hashed_index]:
                if i[0] == cur_query.number:
                    i[1] = cur_query.name
                    continue
            else: # otherwise, just add it
                hash_table[hashed_index].append([cur_query.number,cur_query.name])
                continue
        

        elif cur_query.type == 'del':
            hashed_index = hash_function(cur_query.number)
            for sublist_index, sublist in enumerate(hash_table[hashed_index]):
                if cur_query.number in sublist:
                    del hash_table[hashed_index][sublist_index]
                    continue

        elif cur_query.type == 'find':
            hashed_index = hash_function(cur_query.number)
            for sublist in hash_table[hashed_index]:
                if sublist[0] == cur_query.number:
                    result.append(sublist[1])
                    break
            else:
                result.append("not found")

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

