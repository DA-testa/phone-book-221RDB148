# python3

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

def read_queries():
    # n = int(input())
    # return [Query(input().split()) for i in range(n)]
    return [Query(["add",123,"Bob"]),Query(["add",321,"Obo"]),Query(["add",222,"SDS"])]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.

    # contacts = [Cont(i.number, i.name) for i in queries]
    # contacts = []
    contacts = [[i.number,i.name] for i in queries]

    for i in contacts:
        print(i)
        
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                # if contact.number == cur_query.number:
                #     contact.name = cur_query.name
                #     break
                if contact[0] == cur_query.number:
                    contact[1] = cur_query.name
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        elif cur_query.type == 'find':
            pass
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

