import matplotlib.pyplot as plt
import networkx as nx
import EoN

nodesLeaf = []
nodes = []
g = nx.Graph()


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.degree = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        self.degree = len(self.children)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level

    def preorder(self):
        spaces = " " * self.get_level()
        prefix = spaces + "|_" if self.parent != None else ""

        if (self.degree == 0):
            nodesLeaf.append(self.data)

        print(f"{prefix} {self.data} (Nível: {self.get_level()}) (Grau: {self.degree})")
        if (len(self.children) > 0):
            for child in self.children:
                child.preorder()

    def subtree(self, target, tree):
        if (tree.get_root().data == target):
            tree.get_root().preorder()
        else:
            if (len(self.children) >= 0):
                for child in self.children:
                    if (child.data == target):
                        child.preorder()
                    else:
                        child.subtree(target, tree)


def add_recursive(nA, nB):
    try:
        while True:
            nFSS = Node(input(f"Nó Filho de {nB.data}\n:"))
            if (nFSS.data == "-1"):
                break

            nodes.append((nB.data, nFSS.data))

            nB.add_child(nFSS)
            add_recursive(nFSS, nA)

        if (nA == None):
            return
    except KeyboardInterrupt as e:
        pass


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self):
        self.root = Node(input("Nó Raiz\n:"))

    def get_root(self):
        return self.root

    def generate(self):
        try:
            while True:
                n = Node(input(f"Nó Filho de {self.root.data}\n:"))
                if (n.data == "-1"):
                    break
                nodes.append((self.root.data, n.data))
                self.root.add_child(n)
                add_recursive(self.root, n)
            return self.root
        except KeyboardInterrupt as e:
            return self.root


class Program:
    def __init__(self):
        pass

    def run(self):
        t = Tree()
        t.set_root()
        t.generate().preorder()

        try:
            g.add_edges_from(nodes)

            pos = EoN.hierarchy_pos(g, t.get_root().data)
            nx.draw(g, pos=pos, with_labels=True)
            plt.draw()
            plt.show()
        except TypeError as e:
            pass

        print(f"\nNó Raiz: \n{t.get_root().data}")
        print("\nNós Folhas:")
        for i in nodesLeaf:
            print(i, end=" ")

        subTree = input("\nSub Árvore do Nó\n:")
        t.get_root().subtree(subTree, t)


if __name__ == "__main__":
    p = Program()
    p.run()
