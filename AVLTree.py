#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        """DEFINIÇÃO DE NÓ."""
        self.data = data
        self.children = [None, None]
        self.height = 1
        self.parent = None

    def get_level(self):
        """PEGAR O NÍVEL DO NÓ."""
        level = 0
        p = self.parent

        while p != None:
            level += 1
            p = p.parent

        return level


class AVLTree:
    def __init__(self, root):
        """DEFINIÇÃO DO NÓ RAIZ DA ÁRVORE."""
        self.root = root

    def insert(self, node, data):
        """INSERÇÃO DE NÓS."""
        if node == None:
            return Node(data)
        elif data < node.data:
            node.children[0] = self.insert(node.children[0], data)
            node.children[0].parent = node
        else:
            node.children[1] = self.insert(node.children[1], data)
            node.children[1].parent = node

        node.height = 1 + max(self.get_height(node.children[0]), self.get_height(node.children[1]))

        # REGRAS DE BALANCEAMENTO
        balanceFactor = self.get_balance_factor(node)

        # ROTAÇÃO PARA DIREITA
        if balanceFactor > 1:
            if data < node.children[0].data:
                return self.right_rotate(node)

            if data > node.children[0].data:
                node.children[0] = self.left_rotate(node.children[0])
                return self.right_rotate(node)

        # ROTAÇÃO PARA ESQUERDA
        if balanceFactor < -1:
            if data > node.children[1].data:
                return self.left_rotate(node)
        
            if data < node.children[1].data:
                node.children[1] = self.right_rotate(node.children[1])
                return self.left_rotate(node)

        return node

    def get_height(self, node):
        """ALTURA DO NÓ."""
        if node == None:
            return 0

        return node.height

    def get_balance_factor(self, node):
        """FATOR DE BALANCEAMENTO."""
        if node == None:
            return 0

        return self.get_height(node.children[0]) - self.get_height(node.children[1])

    def left_rotate(self, node):
        """ROTAÇÃO SIMPLES PARA ESQUERDA."""

        # PEGA O PARENTE DO PIVÔ
        aux = node.parent

        # NÓ DIREITO DO PIVÔ
        node_right = node.children[1]

        # PARTE ESQUERDA DO NÓ DIREITO DO PIVÔ
        if_node_right_left_exists = node_right.children[0]

        # NÓ DIREITO VAI PARA O PIVÔ
        node_right.children[0] = node

        # O PARENTE DO PIVÔ SERÁ O NÓ DIREITO
        node.parent = node_right

        # O NÓ DIREITO DO PIVÔ SERÁ O NÓ ESQUERDO DO NÓ DIREITO DO PIVÔ (CASO EXISTA)
        # CASO NÃO EXISTA É REMOVIDO (NONE)
        node.children[1] = if_node_right_left_exists

        # CASO EXISTA, O PARENTE DO NÓ DIREITO DO NÓ ESQUERDO DO PIVÔ É O PIVÔ
        if if_node_right_left_exists != None:
            if_node_right_left_exists.parent = node

        # O PARENTE DO NÓ DIREITO DO PIVÔ SERÁ O PARENTE DO PIVÔ
        node_right.parent = aux

        # CASO NÃO TENHA UM PARENTE NO NÓ DIREITO DO PIVÔ O SIGNIFICA QUE ELE É O NOVO NÓ RAIZ DA ÁRVORE
        if node_right.parent == None:
            self.root = node_right

        # ATUALIZANDO ALTURAS
        node.height = 1 + max(self.get_height(node.children[0]), self.get_height(node.children[1]))
        node_right.height = 1 + max(self.get_height(node_right.children[0]), self.get_height(node_right.children[1]))

        return node_right

    def right_rotate(self, node):
        """ROTAÇÃO SIMPLES PARA DIREITA."""

        # PEGA O PARENTE NÓ
        aux = node.parent

        # NÓ ESQUERDO DO PIVÔ
        node_left = node.children[0]

        # PARTE DIREITA DO NÓ ESQUERDO DO PIVÔ
        if_node_left_right_exists = node_left.children[1]

        # PIVÔ VAI PARA O NÓ DIREITO DO NÓ ESQUERDO DO PIVÔ
        node_left.children[1] = node

        # O PARENTE DO PIVÔ SERÁ O NÓ ESQUERDO
        node.parent = node_left

        # O NÓ ESQUERDO DO PIVÔ SERÁ O NÓ DIREITO DO NÓ ESQUERDO DO PIVÔ (CASO EXISTA)
        # CASO NÃO EXISTA É REMOVIDO (NONE)
        node.children[0] = if_node_left_right_exists

        # CASO EXISTA, O PARENTE DO NÓ DIREITO DO NÓ ESQUERDO DO PIVÔ É O PIVÔ
        if if_node_left_right_exists != None:
            if_node_left_right_exists.parent = node

        # O PARENTE DO NÓ ESQUERDO DO PIVÔ SERÁ O PARENTE DO PIVÔ
        node_left.parent = aux

        # CASO NÃO TENHA UM PARENTE NO NÓ ESQUERDO DO PIVÔ O SIGNIFICA QUE ELE É O NOVO NÓ RAIZ DA ÁRVORE
        if node_left.parent == None:
            self.root = node_left

        # ATUALIZANDO ALTURAS
        node.height = 1 + max(self.get_height(node.children[0]), self.get_height(node.children[1]))
        node_left.height = 1 + max(self.get_height(node_left.children[0]), self.get_height(node_left.children[1]))

        return node_left

    def pre_order(self, root, direction=None):
        """PRINTANDO A ÁRVORE EM PRÉ-ORDEM."""
        if root == None:
            return

        spaces = " " * root.get_level()
        prefix = spaces + "|_" if root.parent != None else ""

        if (direction == "left"):
            print(f"{prefix} {root.data} (esquerdo)")
        elif (direction == "right"):
            print(f"{prefix} {root.data} (direito)")
        else:
            print(f"{prefix} {root.data}")

        self.pre_order(root.children[0], "left")
        self.pre_order(root.children[1], "right")


# NÓ RAIZ
root = int(input("Nó raiz:"))

# CRIANDO ÁRVORE E INSERINDO O NÓ RAIZ.
Tree = AVLTree(root)
t = None
t = Tree.insert(None, root)

# "CAUDA DA ÁRVORE."
while True:
    node = int(input("Nó:"))
    if (node < 0):
        break
    t = Tree.insert(t, node)

# PRINTANDO A ÁRVORE EM PRÉ-ORDEM.
Tree.pre_order(t)
