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
