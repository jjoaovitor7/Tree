nodesLeaf = []


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


def add_recursive(nA, nB):
    try:
        while True:
            nFSS = Node(input(f"Nó Filho de {nA.data}\n:"))
            if (nFSS.data == "-1"):
                break

            nB.add_child(nFSS)
            add_recursive(nFSS, nA)

        if (nA == None):
            return
    except KeyboardInterrupt as e:
        pass


class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self):
        self.root = Node(input("Nó Raiz\n:"))

    def getRoot(self):
        return self.root

    def generate(self):
        try:
            while True:
                n = Node(input("Nó Filho\n:"))
                if (n.data == "-1"):
                    break
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
        t.setRoot()
        t.generate().preorder()

        print(f"\nNó Raiz: \n{t.getRoot().data}")
        print("\nNós Folhas:")
        for i in nodesLeaf:
            print(i, end=" ")


if __name__ == "__main__":
    p = Program()
    p.run()
