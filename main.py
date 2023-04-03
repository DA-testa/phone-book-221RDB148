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
    # n = int(input())
    # return [Query(input().split()) for i in range(n)]
    return [Query(["add",123,"Bob"]),Query(["add",321,"Obo"]),Query(["add",222,"SDS"]),Query(["find",321])]

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
                    return
            else: # otherwise, just add it
                hash_table[hashed_index].append([cur_query.number,cur_query.name])
        

        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break


        elif cur_query.type == 'find':
            hashed_index = hash_function(cur_query.number)
            for i in hash_table[hashed_index]:
                if i[0] == cur_query.number:
                    # return i[1]
                    print(i[1])
                else:
                    print("wasnt found")
        
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

