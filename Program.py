from sys import getsizeof
from Tree import Tree

def count_keys(dict_, counter=0):
    for each_key in dict_:
        if isinstance(dict_[each_key], dict):
            counter = count_keys(dict_[each_key], counter + 1)
        else:
            counter += 1
    return counter


class Program():
    def __init__(self):
        pass

    def run(self):
        _tree = dict()
        tree = Tree(_tree)
        exec = True

        while (exec):
            opt = int(input("""Opções
 1: Adicionar Nó
 2: Visualizar Nós
 3: Visualizar Níveis
 4: Visualizar Graus
 5: Visualizar Nós Folhas
 6: Visualizar Representação Gráfica
 7: Visualizar Subárvore de Nó
99: Sair
:"""))

            if (opt == 1):
                while(True):
                    node = input("Nó:")

                    if (node == ""):
                        node = None

                    if (node != "-1"):
                        if (len(_tree) == 0):
                            _tree[node] = {}
                        else:
                            def add(d, l):
                                if (isinstance(d, str) and not(node in list(l))):
                                    c = list(l.copy())
                                    global p
                                    if (count_keys(l[c[0]]) == 2):
                                        p = c.pop(0)

                                    if (count_keys(l[c[0]]) < 2):
                                        l[c[0]][node] = {}
                                    else:
                                        if (p != None):
                                            _iter = iter(l[p])

                                            while (True):
                                                try:
                                                    l[p][next(_iter)][node] = {}
                                                    break
                                                except StopIteration:
                                                    add(node, l[p])
                                                    break

                                else:
                                    if (l != None and node in list(l)):
                                        pass
                                    else:
                                        for key, value in d.items():
                                            if (isinstance(value, dict)):
                                                if (count_keys(value) < 2):
                                                    if (None in value):
                                                        del value[None]
                                                    value[node] = {}

                                                else:
                                                    if (None in value):
                                                        del value[None]
                                                        value[node] = {}
                                                    else:
                                                        add(node, value)
                            add(_tree, None)

                    if (node == "-1"):
                        break

            if (opt == 2):
                print("Nós:")
                nodes = tree.getNodes()
                for i in nodes:
                    print(i, end=" ")

            elif (opt == 3):
                print("\nNíveis:")
                levels = tree.getLevels()
                for i in range(len(levels)):
                    for j in levels[i]:
                        print(j, end=" ")
                    print("|", end=" ")

            elif (opt == 4):
                print("\nGraus:")
                degrees = tree.getDegrees()
                for i in range(len(degrees)):
                    for j in degrees[i]:
                        print(j, end=" ")
                    print("|", end=" ")

            elif (opt == 5):
                print("\nNós Folhas:")
                for i in tree.getLeafNodes():
                    print(i, end=" ")

            elif (opt == 6):
                try:
                    tree.generateGraph()
                except:
                    pass

            elif (opt == 7):
                node = input("Nó:")
                print(tree.getSubTree(node))

            elif (opt == 99):
                break

            else:
                print("Opção não encontrada.")

            print("\n")


if __name__ == "__main__":
    p = Program()
    p.run()
