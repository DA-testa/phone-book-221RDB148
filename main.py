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
######################################################
#     n = 12
#     s = """add 911 police
# add 76213 Mom
# add 17239 Bob
# find 76213
# find 910
# find 911
# del 910
# del 911
# find 911
# find 76213
# add 76213 daddy
# find 76213"""
#     lines = s.splitlines()
#     # queries = [Query(line.split()) for line in lines]
#     queries = [[] for i in range(n)]
#     k=0
#     for i in lines:
#         queries[k] = i
#         k=k+1
#######################################################
    # return [Query(["add",123,"Bob"]),
    #         Query(["add",321,"Obo"]),
    #         Query(["add",222,"SDS"]),
    #         Query(["find",321]),
    #         Query(["add",523,"vdf"]),
    #         Query(["add",532,"bfj"]),
    #         Query(["add",660,"ged"]),
    #         Query(["add",896,"vdv"]),
    #         Query(["find",660]),
    #         Query(["find",000]),
    #         Query(["del",523]),]
#######################################################
    # return [Query(["add",911,"police"]),
    #         Query(["add",76213,"Mom"]),
    #         Query(["add",17239,"Bob"]),
    #         Query(["find",76213]),
    #         Query(["find",910]),
    #         Query(["find",911]),
    #         Query(["del",910]),
    #         Query(["del",911]),
    #         Query(["find",911]),
    #         Query(["find",76213]),
    #         Query(["add",76213,"daddy"]),
    #         Query(["find",76213]),]
#######################################################
    # return [Query(["find",3839442]),
    #         Query(["add",123456,"me"]),
    #         Query(["add",0,"granny"]),
    #         Query(["find",123456]),
    #         Query(["find",123456]),
    #         Query(["del",0]),
    #         Query(["del",0]),
    #         Query(["find",0]),]


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

