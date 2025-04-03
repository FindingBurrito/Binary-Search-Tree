
import random

# Node Class
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# Binarysearchtree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_new_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        done_with_new_node = False

        while not done_with_new_node:
            if value < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    done_with_new_node = True
                else:
                    temp = temp.left
            elif value > temp.data:
                if temp.right is None:
                    temp.right = new_node
                    done_with_new_node = True
                else:
                    temp = temp.right
            else:
                print(f"{value} is already in the tree; Duplicates not allowed")
                done_with_new_node = True

    def traverse_preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node):
        if node:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=' ')

    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print(node.data, end=' ')
            self.traverse_inorder(node.right)

# Main Function
def main():
    BST = BinarySearchTree()

    with open("tree_values.txt", "r") as file:
        for line in file:
            value = int(line.strip())
            BST.insert_new_node(value)

    print("Preorder:", end=' ')
    BST.traverse_preorder(BST.root)
    print()

    print("Postorder:", end=' ')
    BST.traverse_postorder(BST.root)
    print()

    print("Inorder:", end=' ')
    BST.traverse_inorder(BST.root)
    print()

if __name__ == "__main__":
    main()
