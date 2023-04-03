import random

# def hash_func(s):

#     x = 0.0
#     for c in s:
#         x = (x * 4 + ord(c)) %17
#         return x % 10


# numbers = ["hkq","bqo","oqp","pwb","vka","viq","qbx","vkq","asd"]

# list = []
# for i in numbers:
#     a = hash_func(i)
#     list.append(a)

# def find(string):
#     hashed = hash_func(string)

################################################################

class Cont:
    def __init__(self, number, name):
        self.number = number
        self.name = name

n0 = Cont(22143566,"VALTERS")
n1 = Cont(27714848,"Karlis")
n2 = Cont(34572356,"Janis")
n3 = Cont(46252462,"Andrejs")
n4 = Cont(74562267,"Ralfs")
n5 = Cont(34563722,"Everts")
n6 = Cont(24564243,"Oto")
n7 = Cont(74663452,"Liene")
n8 = Cont(87458212,"Sandijs")
n9 = Cont(23576857,"Efraims")

n10 = Cont(23456893,"Kaķis")
n11 = Cont(84750367,"Māja")
n12 = Cont(93476093,"Diāna")
n13 = Cont(83467922,"Nauris")
n14 = Cont(98705467,"Timotejs")
n15 = Cont(24561809,"Everts")
n16 = Cont(73655624,"Viktorija")
n17 = Cont(37494087,"Janka")
n18 = Cont(98487078,"Rūdolfs")
n19 = Cont(73694059,"Kāja")

prime = 23
# a = random.randint(1, prime-1)
# b = random.randint(0, prime-1)
a =1
b = 8
def h(x):
    hashValue = (a*x + b)%prime
    return hashValue%len(list)

list = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19]

actual = [0] * len(list)

for i in range(0,len(list)):
    print(i   ,   end="")
    for obj in list:
        if h(obj.number) == i:
            print("(",obj.number,obj.name,")",end="")
            actual[i] = list[i]
    
    print()




def findName(numb):
    value = h(numb)
    print(list[value].name, value)

findName(22143566)


l=-1
for i in actual:
    l=l+1
    if i is None:
        print(i, "is empty")
        continue
    if isinstance(i, Cont):
        print(l, " ",i.number, i.name)
        continue
    print(l)
