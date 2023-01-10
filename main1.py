import networkx as nx
from dataclasses import dataclass
import matplotlib.pyplot as plt
# import matplotlib
# from .UnionFind import UnionFind

# matplotlib.use('Qt5Agg')
@dataclass(order=True, slots=True)
class Node:
    val: int
    is_start: bool

def main():
    N, Q = tuple(map(int, input().split(" ")))

    G = nx.DiGraph()

    list_set: set[tuple[int]] = set()
    len_set: set[int] = set()

    for i in range(N):
        P = tuple(map(int, input().split(" ")))
        P, list_int = P[0], P[1:]

        G.add_nodes_from(list_int)

        for i in list_int[1:]:
            G.add_edge(list_int[0], i)

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

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
