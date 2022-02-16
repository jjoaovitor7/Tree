import matplotlib.pyplot as plt
import networkx as nx

class Tree:
    def __init__(self, tree):
        self.tree = tree
        self.nodes = []
        self.nodesLevels = []
        self.nodesDegrees = []
        self.nodesLeaf = []

    def getRoot(self):
        return next(iter(self.tree.keys()))

    def getNodes(self):
        def getNodes__aux(d):
            for key, value in d.items():
                # RETORNA O VALOR DA KEY E CONTINUA A EXECUÇÃO
                yield key

                # CASO O VALUE SEJA UM DICT
                if isinstance(value, dict):
                    # FAZ A RECURSÃO ATÉ QUE NÃO RESTE MAIS NENHUM ELEMENTO NO DICT
                    yield from getNodes__aux(value)
                else:
                    yield value

        # PARA CADA ELEMENTO QUE FOR RETORNADO NA FUNÇÃO GERADORA
        for i in getNodes__aux(self.tree):
            # ADICIONE-O NA LISTA
            self.nodes.append(i)

        return self.nodes

    def getLevels(self):
        def getLevels__aux(d, level=0):
            for key, value in d.items():
                # RETORNA O VALOR DA KEY E CONTINUA A EXECUÇÃO
                yield [key, level]

                # CASO O VALUE SEJA UM DICT
                if isinstance(value, dict):
                    # FAZ A RECURSÃO ATÉ QUE NÃO RESTE MAIS NENHUM ELEMENTO NO DICT
                    yield from getLevels__aux(value, level+1)
                else:
                    yield [value, level]

        for i in getLevels__aux(self.tree):
            self.nodesLevels.append(i)

        return self.nodesLevels

    def getDegrees(self):
        def getDegrees__aux(d):
            for key, value in d.items():
                # RETORNA O VALOR DA KEY E CONTINUA A EXECUÇÃO
                yield [key, len(value)]

                # CASO O VALUE SEJA UM DICT
                if isinstance(value, dict):
                    # FAZ A RECURSÃO ATÉ QUE NÃO RESTE MAIS NENHUM ELEMENTO NO DICT
                    yield from getDegrees__aux(value)
                else:
                    yield [value, 0]

        for i in getDegrees__aux(self.tree):
            self.nodesDegrees.append(i)

        return self.nodesDegrees

    def getLeafNodes(self):
        for i in self.nodesDegrees:
            if (i[1] == 0):
                self.nodesLeaf.append(i[0])
        return self.nodesLeaf


tree = Tree({"n1": {"n2": {"n5": "n6"}, "n3": {
            "n7": {"n8": {"n9": "n10"}}}, "n4": "n11"}})

print("Nós:")
tree.getNodes()
for i in tree.getNodes():
    print(i, end=" ")

print("\nNíveis:")
levels = tree.getLevels()
for i in range(len(levels)):
    for j in levels[i]:
        print(j, end=" ")
    print("|", end=" ")

print("\nGraus:")
degrees = tree.getDegrees()
for i in range(len(degrees)):
    for j in degrees[i]:
        print(j, end=" ")
    print("|", end=" ")

print("\nNós Folhas:")
for i in tree.getLeafNodes():
    print(i, end=" ")

g = nx.Graph()
g.add_nodes_from(tree.tree.keys())

q = list(tree.tree.items())
while q:
    v, d = q.pop()
    for nv, nd in d.items():
        if (isinstance(nd, dict)):
            q.append((nv, nd))
        else:
            g.add_edge(nv, nd)
        g.add_edge(v, nv)

nx.draw(g, with_labels=True)
plt.draw()
plt.show()