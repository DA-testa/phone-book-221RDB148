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
    #         Query(["find",000]),]


def write_responses(result):
    print()
    print('\n'.join(result))

def process_queries(queries):
    # declare hash table with size
    size = 0
    for cur_query in queries:
        if cur_query.type == 'add':
            size = size + 1
    
    print(size)
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
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = [Cont(i.number, i.name) for i in queries]
    # contacts = []
    # contacts = [[i.number,i.name] for i in queries]
    # for i in contacts:
    #     print(i)

    for cur_query in queries:
        if cur_query.type == 'add':
            hashed_index = hash_function(cur_query.number)
            # if we already have contact with such number,
            # we should rewrite contact's name
            for i in hash_table[hashed_index]:
                if i[0] == cur_query.number:
                    i[1] = cur_query.name
                    continue
            else: # otherwise, just add it
                hash_table[hashed_index].append([cur_query.number,cur_query.name])
                continue
        

        elif cur_query.type == 'del':
            hashed_index = hash_function(cur_query.number)
            for i in hash_table[hashed_index]:
                if cur_query.number in i:
                    hash_table.remove[i]
                    print("removed")
                    continue



        elif cur_query.type == 'find':
            hashed_index = hash_function(cur_query.number)
            k=0
            for i in hash_table[hashed_index]:
                if i[0] == cur_query.number:
                    # return i[1]
                    print(i[1])
                    result.append(i[1])
                    k=k + 1
            if k==0: 
                print("not found")
                result.append("not found")
        
        # else:
        #     response = 'not found'
        #     print("not found")
        #     for contact in contacts:
        #         if contact.number == cur_query.number:
        #             response = contact.name
        #             break
        #     result.append(response)
        # print("not asdasd", cur_query.type)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

