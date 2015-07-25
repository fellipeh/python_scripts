#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def show_tree(self):
        if self.left:
            self.left.show_tree()

        print self.data

        if self.right:
            self.right.show_tree()

    def compare_two_trees(self, node):
        """
        ToDo: Need to be verified and tested!
        """
        if node is None:
            return False

        if self.data != node.date:
            return False

        result = True

        if self.left is None:
            if node.left:
                return False
        else:
            result = self.left.compare_two_trees(node.left)

        if result is False:
            return False

        if self.right is None:
            if node.right:
                return False
        else:
            result = self.right.compare_two_trees(node.right)
        return result

# test
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)

# print all tree
root.show_tree()
