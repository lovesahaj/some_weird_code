class UnionFind:
    __slots__ = ("__elements", "__count")

    def __init__(self) -> None:
        self.__elements: dict = {}
        self.__count = 0

    def increaseSet(self, newElements):
        for element in newElements:
            self.__elements[element] = {
                "parent": element,
                "size": 1,
            }

            self.__count += 1

    def count(self) -> int:
        return self.__count

    def find(self, p) -> int:
        # self.__validate(p)

        while p != self.__elements[p]["parent"]:
            p = self.__elements[p]["parent"]

        return p

    def connected(self, p, q) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p, q) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        if self.__elements[rootP]['size'] < self.__elements[rootQ]['size']:
            self.__elements[rootP]['parent'] = rootQ
            self.__elements[rootQ]['size'] += self.__elements[rootP]['size']

        else:
            self.__elements[rootQ]['parent'] = rootP
            self.__elements[rootP]['size'] += self.__elements[rootQ]['size']

        self.__count -= 1


    def display(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        
        graph = nx.DiGraph()

        for u in self.__elements:
            graph.add_edge(u, self.__elements[u]['parent'])


        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
