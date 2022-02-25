nodesLeaf = []

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.degree = 0
        self.nodesLeaf = []

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

        print(f"{prefix} {self.data} {self.get_level()} {self.degree}")
        if (len(self.children) > 0):
            for child in self.children:
                child.preorder()

    def get_nodesLeaf(self):
        return self.nodesLeaf


def add__recursive(nA, nB):
    for k in nA.children:
        nFSubSub = input(f"Nó Filho de {k.data}\n:")
        if (nFSubSub == "-1"):
            break
        global nFSubSubNode
        nFSubSubNode = Node(nFSubSub)
        nB.add_child(nFSubSubNode)

    if (len(nA.children) != 0):
        return
    else:
        add__recursive(nFSubSubNode, nA)


def Tree():
    root = Node(input("Nó Raiz\n:"))

    nn = None
    while True:
        n = input("Nó Filho\n:")
        if (n == "-1"):
            break
        nn = Node(n)

        for i in root.children:
            nF = input(f"Nó Filho de {i.data}\n:")
            if (nF == "-1"):
                break
            nFNode = Node(nF)
            nn.add_child(nFNode)
            for j in nn.children:
                nFSub = input(f"Nó Filho de {j.data}\n:")
                if (nFSub == "-1"):
                    break
                nFSubNode = Node(nFSub)
                nFNode.add_child(nFSubNode)
                add__recursive(nFNode, nFSubNode)

        root.add_child(nn)

    return root


class Program:
    def __init__(self):
        pass

    def run(self):
        Tree().preorder()

        print("Nós Folhas:")
        for i in nodesLeaf:
            print(i, end=" ")


if __name__ == "__main__":
    p = Program()
    p.run()
