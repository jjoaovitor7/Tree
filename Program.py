#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import EoN
import random

# NÓS FOLHAS.
nodesLeaf = []

# ARRAY DE TUPLAS PARA REPRESENTAÇÃO GRÁFICA DO NÓ.
nodes = []

# REPRESENTAÇÃO GRÁFICA DO NÓ.
g = nx.Graph()

# PARA EVITAR NÓS DUPLICADOS.
avoidDuplicates = []


class Node:
    def __init__(self, data):
        """
        CONSTRUTOR DA CLASSE.
        """
        self.data = data
        self.children = []
        self.parent = None
        self.degree = 0

    def add_child(self, child):
        """
        FUNÇÃO RESPONSÁVEL POR ADICIONAR FILHOS AO NÓ.
        O PAI DO NÓ SERÁ O NÓ BASE A ELE
        POR ISSO 'child.parent = self', EM OUTRAS PALAVRAS
        É PEGO O NÓ BASE E É COLOCADO COMO PAI DO NÓ ATUAL.
        """
        child.parent = self
        self.children.append(child)

        # O GRAU É DETERMINADO PELA QUANTIDADE DE FILHOS QUE O NÓ APRESENTA.
        self.degree = len(self.children)

    def get_level(self):
        """
        FUNÇÃO RESPONSÁVEL PELA OBTENÇÃO DO NÍVEL DE CADA NÓ.
        """
        level = 0
        p = self.parent

        # ENQUANTO O NÓ ANTERIOR TIVER ALGUM NÓ BASE ANTES DELE
        # O NÍVEL É INCREMENTADO
        # ATÉ QUE NÃO APRESENTE MAIS NENHUM NÓ BASE ANTES DELE.
        while p:
            level += 1
            p = p.parent

        # SE NÃO TIVER MAIS NENHUM NÓ BASE, RETORNE O LEVEL.
        return level

    def get_height(self):
        """FUNÇÃO RESPONSÁVEL POR RETORNAR A ALTURA DO NÓ."""
        l = []
        for c in self.children:
            l.append(c.get_height())

        # [] FAZ RETORNAR O DEFAULT (-1), 1 + -1 = 0
        # l = [0]
        # DEPOIS DISSO ELE VAI CONSIDERANDO MAX DE l
        # max(l) = 0, 1 + 0 = 1
        # max(l) = 1, 1 + 1 = 2
        # ...
        # CASO TENHA UM NÓ IRMÃO,
        # ADICIONE o max(l) DO NÓ IRMÃO TAMBÉM AO l
        # ex. l = [2, 0]

        height = 1 + max(l, default=-1)
        return height

    def preorder(self):
        """
        FUNÇÃO RESPONSÁVEL POR PRINTAR A ÁRVORE EM PRÉ-ORDEM.
        """

        spaces = " " * self.get_level()
        prefix = spaces + "|_" if self.parent != None else ""

        # CASO O GRAU DÓ NÓ SEJA 0 ELE É UM NÓ FOLHA.
        if (self.degree == 0):
            nodesLeaf.append(self.data)

        print(
            f"{prefix} {self.data} (Nível | Profundidade: {self.get_level()}) (Grau: {self.degree})")
        if (len(self.children) > 0):
            for child in self.children:
                child.preorder()

        # VOLTA DA PILHA DA RECURSÃO (CALL STACK).
        global h
        h = self.get_height()

    def subtree(self, target, tree):
        """FUNÇÃO RESPONSÁVEL POR PRINTAR A SUBÁRVORE DE UM DETERMINADO NÓ."""
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
    """FUNÇÃO RESPONSÁVEL PELA ADIÇÃO DE NÓS DE FORMA RECURSIVA."""
    try:
        while True:
            # nFSS = Node(input(f"Nó Filho de {nB.data}\n:"))
            nFSS = Node(random.choice([str(random.randrange(50)), "-1"]))
            if (nFSS.data == "-1"):
                break

            # len(nB.children) < 2, ÁRVORE BINÁRIA.
            if (nFSS.data not in avoidDuplicates and len(nB.children) < 2):
                avoidDuplicates.append(nFSS.data)
                nodes.append((nB.data, nFSS.data))
                nB.add_child(nFSS)

                add_recursive(nFSS, nA)
            else:
                add_recursive(nA, nB)

        if (nA == None):
            return
    except KeyboardInterrupt as e:
        # PARA NÃO TER QUE FICAR DIGITANDO -1 TODA HORA.
        print("")


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self):
        """FUNÇÃO RESPONSÁVEL POR SETAR O NÓ RAIZ."""
        # self.root = Node(input("Nó Raiz\n:"))

        self.root = Node(str(random.randrange(50)))

        if (self.root in avoidDuplicates):
            self.set_root()
        else:
            avoidDuplicates.append(self.root.data)

    def get_root(self):
        """FUNÇÃO RESPONSÁVEL POR OBTER O NÓ RAIZ."""
        return self.root

    def generate(self):
        """FUNÇÃO RESPONSÁVEL PELA ENTRADA DE DADOS E GERAÇÃO DA ÁRVORE."""
        try:
            while True:
                # n = Node(input(f"Nó Filho de {self.root.data}\n:"))
                n = Node(random.choice([str(random.randrange(50)), "-1"]))

                if (n.data == "-1"):
                    break

                # len(self.get_root().children) < 2, ÁRVORE BINÁRIA.
                if (n.data not in avoidDuplicates and len(self.get_root().children) < 2):
                    avoidDuplicates.append(n.data)
                    nodes.append((self.root.data, n.data))
                    self.root.add_child(n)
                    add_recursive(self.root, n)
                else:
                    self.generate()
            return self.root
        except KeyboardInterrupt as e:
            return self.root


class Program:
    def __init__(self):
        pass

    def run(self):
        t = Tree()

        # SETANDO NÓ RAIZ.
        t.set_root()

        # GERANDO ÁRVORE E A PRINTANDO EM PRÉ-ORDEM.
        tg = t.generate()
        tg.preorder()

        # REPRESENTAÇÃO GRÁFICA.
        try:
            g.add_edges_from(nodes)

            pos = EoN.hierarchy_pos(g, t.get_root().data)
            nx.draw(g, pos=pos, with_labels=True)
            plt.draw()
            plt.show()
        except (TypeError, nx.exception.NetworkXPointlessConcept) as e:
            print("Erro ao gerar a representação gráfica.")

        # NÓ RAIZ.
        print(f"\nNó Raiz: \n{t.get_root().data}")

        # NÓ FOLHAS.
        print("\nNós Folhas:")
        for i in nodesLeaf:
            print(i, end=" ")

        # SUB ÁRVORE DE DETERMINADO NÓ.
        while True:
            try:
                sT = input("\n\nSub Árvore e Altura do Nó\n:")

                if (sT == "-1"):
                    break

                if (sT in avoidDuplicates):
                    print(f"\nSub Árvore do Nó {sT}:\n")
                    t.get_root().subtree(sT, t)
                    print(f"\nAltura do Nó {sT}:\n{h}")
            except KeyboardInterrupt as e:
                break


if __name__ == "__main__":
    p = Program()
    p.run()
