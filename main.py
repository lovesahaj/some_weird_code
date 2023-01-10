from dataclasses import dataclass
from typing import List, Tuple, Set 

def main():
    N, Q = tuple(map(int, input().split(" ")))

    list_set: Set = set()
    len_set: Set= set()

    for i in range(N):
        P = tuple(map(int, input().split(" ")))
        P, list_int = P[0], P[1:]

        len_set.add(P)
        list_set.add(list_int)

    for i in range(Q):
        Q = tuple(map(int, input().split(" ")))
        Q, list_int = Q[0], Q[1:]

        if Q not in len_set:
            len_set.add(Q)
            list_set.add(list_int)

        elif list_int not in list_set:
            list_set.add(list_int)

        print(list_set)



if __name__ == "__main__":
    main()
