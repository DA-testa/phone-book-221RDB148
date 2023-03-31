class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

n = 2
str = "add 1234 Bob"
a = [Query(str.split()) for i in range(n)]
# print(a)
# print(Query(str.split()).name)
query1 = Query(['add', '123', 'John Doe'])
query2 = Query(['add', '321', 'John Doe'])
query3 = Query(['add', '789', 'John Doe'])
query4 = Query(['add', '552', 'John Doe'])
