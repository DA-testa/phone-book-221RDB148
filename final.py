import random



def randContacts():
    phone_list = []
    for i in range(1000):
        numb = random.randint(0,9999999)
        nam = random.randint(0,999)
        phone_list.append([numb,nam])
    phone_list[1] = [12345,343]
    return phone_list

def next_prime(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = num + 1
    while True:
        if is_prime(n):
            return n
        n += 1

phone_list = randContacts()

#declares size
size = len(phone_list)

table = [[] for i in range(size)]

p = next_prime(size)
a = random.randint(1, p - 1)
b = random.randint(0, p - 1)

def hash_function(number):
    return ((a * hash(number) + b) % p) % size

def hash_add(number, name):
    global table
    index = hash_function(number)
    for i in table[index]:
        if i[0] == number:
            i[1] = name
            return
    table[index].append([number, name])

def hash_get(number):
    global table
    index = hash_function(number)
    for i in table[index]:
        if i[0] == number:
            return i[1]
        else:
            print("wasnt found")


for name, number in phone_list:
    hash_add(name, number)

def hash_print():
    l=0
    k = 0
    for i in table:
        if len(i) > k:
            k = len(i)
        # print(l," ",i)
        l = l + 1
    print("longest collision:",k)

hash_print()
