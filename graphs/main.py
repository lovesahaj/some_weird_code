from typing import Set
from UnionFind import UnionFind


def addListToSet(disSet, parent, arr):
    for i in arr:
        disSet.union(parent, i)


def initalization(inputs):
    list_set: Set = set()
    len_set: Set = set()
    disjointSet = UnionFind()

    for i in inputs:
        length, list_int = i[0], i[1:]

        len_set.add(length)
        list_set.add(list_int)
        parent = list_int[0]
        disjointSet.increaseSet(list_int)
        addListToSet(disjointSet, parent, list_int)

    return list_set, len_set, disjointSet


def querying(
    len_set,
    list_set,
    disjointSet,
    len_query,
    query,
):
    if len_query not in len_set:
        len_set.add(len_query)
        list_set.add(query)
        parent = query[0]
        addListToSet(disjointSet, parent, query)

    elif query not in list_set:
        list_set.add(query)
        parent = query[0]
        addListToSet(disjointSet, parent, query)

    print(list_set)


def main():

    inputs = [
        (3, 1, 2, 3),
        (2, 4, 5),
        (4, 6, 7, 8, 9),
    ]

    list_set, len_set, disjointSet = initalization(inputs)


    # disjointSet.display()
    queries = [
        (2, 2, 4),
        (2, 4, 5),
        (2, 7, 8),
    ]

    for query in queries:
        querying(len_set, list_set, disjointSet, query[0], query[1:])
        # disjointSet.display()

    print(disjointSet.count())
    # disjointSet.display()

    inputs = [
        (5, 1, 2, 3, 4, 5),
        (7, 6, 7, 8, 9, 10, 11, 12),
        (10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
        (3, 23, 24, 25, 26),
        # (1, 26),
    ]

    list_set, len_set, disjointSet = initalization(inputs)
   
    disjointSet.display()

    queries = [
        # (1, 27, 24),
        (3, 6, 7, 8),
        (3, 2, 8, 15),
        (2, 24, 26),
    ]
    
    for query in queries:
        querying(len_set, list_set, disjointSet, query[0], query[1:])

    disjointSet.display()

# def main():
#     N, Q = tuple(map(int, input().split(" ")))

#     list_set: Set = set()
#     len_set: Set= set()
#     disjointSet = UnionFind()

#     for _ in range(N):
#         P = tuple(map(int, input().split(" ")))
#         P, list_int = P[0], P[1:]
#
#         len_set.add(P)
#         list_set.add(list_int)
#         parent = list_int[0]
#         disjointSet.increaseSet(list_int)
#         addListToSet(disjointSet, parent, list_int)


#     # print(, disjointSet.find(2), disjointSet.find(6))

#     for _ in range(Q):
#         Q = tuple(map(int, input().split(" ")))
#         Q, list_int = Q[0], Q[1:]


#         if Q not in len_set:
#             len_set.add(Q)
#             list_set.add(list_int)
#             parent = list_int[0]
#             addListToSet(disjointSet, parent, list_int)

#         elif list_int not in list_set:
#             list_set.add(list_int)
#             parent = list_int[0]
#             addListToSet(disjointSet, parent, list_int)

#         print(list_set)

#     print(disjointset.count())
#     disjointset.display()

main()
