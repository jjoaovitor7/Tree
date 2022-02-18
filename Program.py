from Tree import Tree

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

                    if (node != "-1"):
                        if (len(_tree) == 0):
                            _tree[node] = {}
                        else:
                            def add(d):
                                aux = None
                                for key, value in d.items():
                                    if (aux != None and aux != key):
                                        break
                                    aux = key
                                    if (len(value) != 2):
                                        d[key][node] = {}
                                    else:
                                        yield from add(value)

                            for i in add(_tree):
                                print(i)

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
                print(_tree)
                tree.generateGraph()

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
