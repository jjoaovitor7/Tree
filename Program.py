#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import EoN

# NÓS FOLHAS.
nodesLeaf = []

# ARRAY DE TUPLAS PARA REPRESENTAÇÃO GRÁFICA DO NÓ.
nodes = []

# REPRESENTAÇÃO GRÁFICA DO NÓ.
g = nx.Graph()

h = []


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
        l = []
        for c in self.children:
            l.append(c.get_height())

        return 1 + max(l, default=-1)

    def preorder(self):
        """
        FUNÇÃO RESPONSÁVEL POR PRINTAR A ÁRVORE EM PRÉ-ORDEM.
        """
        spaces = " " * self.get_level()
        prefix = spaces + "|_" if self.parent != None else ""

        # caso
        if (self.degree == 0):
            nodesLeaf.append(self.data)

        print(
            f"{prefix} {self.data} (Nível | Profundidade: {self.get_level()}) (Grau: {self.degree})")
        if (len(self.children) > 0):
            for child in self.children:
                child.preorder()

        try:
            if (h[0] == -1):
                global hh
                hh = self.get_height()
        except IndexError as e:
            pass

    def subtree(self, target, tree):
        """FUNÇÃO RESPONSÁVEL POR PRINTAR A SUBÁRVORE DE UM DETERMINADO NÓ."""
        if (tree.get_root().data == target):
            h.append(-1)
            tree.get_root().preorder()
        else:
            if (len(self.children) >= 0):
                for child in self.children:
                    if (child.data == target):
                        h.append(-1)
                        child.preorder()
                    else:
                        child.subtree(target, tree)


def add_recursive(nA, nB):
    """FUNÇÃO RESPONSÁVEL PELA ADIÇÃO DE NÓS DE FORMA RECURSIVA"""
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
        # PARA NÃO TER QUE FICAR DIGITANDO -1 TODA HORA.
        print("")


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self):
        """FUNÇÃO RESPONSÁVEL POR SETAR O NÓ RAIZ."""
        self.root = Node(input("Nó Raiz\n:"))

    def get_root(self):
        """FUNÇÃO RESPONSÁVEL POR OBTER O NÓ RAIZ."""
        return self.root

    def generate(self):
        """FUNÇÃO RESPONSÁVEL PELA ENTRADA DE DADOS E GERAÇÃO DA ÁRVORE."""
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

        # SETANDO NÓ RAIZ.
        t.set_root()

        # GERANDO ÁRVORE E A PRINTANDO EM PRÉ-ORDEM.
        t.generate().preorder()

        # REPRESENTAÇÃO GRÁFICA.
        try:
            g.add_edges_from(nodes)

            pos = EoN.hierarchy_pos(g, t.get_root().data)
            nx.draw(g, pos=pos, with_labels=True)
            plt.draw()
            plt.show()
        except TypeError as e:
            pass

        # NÓ RAIZ.
        print(f"\nNó Raiz: \n{t.get_root().data}")

        # NÓ FOLHAS.
        print("\nNós Folhas:")
        for i in nodesLeaf:
            print(i, end=" ")

        # SUB ÁRVORE DE DETERMINADO NÓ.
        subTree = input("\n\nSub Árvore e Altura do Nó\n:")
        print(f"\nSub Árvore do Nó {subTree}:\n")
        t.get_root().subtree(subTree, t)
        try:
            print(f"\nAltura do Nó {subTree}:\n{hh}")
        except NameError as e:
            print("Nó não encontrado.")


if __name__ == "__main__":
    p = Program()
    p.run()
