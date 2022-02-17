from Tree import Tree

tree = Tree({"n1": {"n2": {"n5": "n6"}, "n3": {
            "n7": {"n8": {"n9": {"n10": {}, "n12": {}}}}}, "n4": "n11"}})

exec = True
while (exec):
    opt = int(input("""Opções\n1-Visualizar Nós
2-Visualizar Níveis
3-Visualizar Graus
4-Visualizar Nós Folhas
5-Visualizar Representação Gráfica
6-Visualizar Subárvore de Nó
:"""))

    if (opt == 1):
        print("Nós:")
        nodes = tree.getNodes()
        for i in nodes:
            print(i, end=" ")

    elif (opt == 2):
        print("\nNíveis:")
        levels = tree.getLevels()
        for i in range(len(levels)):
            for j in levels[i]:
                print(j, end=" ")
            print("|", end=" ")

    elif (opt == 3):
        print("\nGraus:")
        degrees = tree.getDegrees()
        for i in range(len(degrees)):
            for j in degrees[i]:
                print(j, end=" ")
            print("|", end=" ")

    elif (opt == 4):
        print("\nNós Folhas:")
        for i in tree.getLeafNodes():
            print(i, end=" ")

    elif (opt == 5):
        tree.generateGraph()

    elif (opt == 6):
        node = input("Nó:")
        print(tree.getSubTree(node))

    else:
        print("Opção não encontrada.")

    print("\n")
