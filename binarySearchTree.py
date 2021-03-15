# Binary Tree implementation using Linked List
# Create Traverse Search Insert Delete
# Binary tree has always at most 2 children

# BST Insert and Delete is much faster than BT
# in BST left side values are less than root node
# and right side is greater than right side
# always working on half of the tree

# this module could be found in the Stack-Queue repo
import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.leftChild is None:
            root_node.leftChild = BSTNode(node_value)
        else:
            insertNode(root_node.leftChild, node_value)
    else:
        if root_node.rightChild is None:
            root_node.rightChild = BSTNode(node_value)
        else:
            insertNode(root_node.rightChild, node_value)
    return "Inserted"


def preOrderTraversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrderTraversal(root_node.leftChild)
    preOrderTraversal(root_node.rightChild)


def inOrderTraversal(root_node):
    if not root_node:
        return
    inOrderTraversal(root_node.leftChild)
    print(root_node.data)
    inOrderTraversal(root_node.rightChild)


def postOrderTraversal(root_node):
    if not root_node:
        return
    postOrderTraversal(root_node.leftChild)
    postOrderTraversal(root_node.rightChild)
    print(root_node.data)


def levelOrderTraversal(root_node):
    if not root_node:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            

def searchNode(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.leftChild.data == node_value:
            print("The value is found")
        else:
            searchNode(root_node.leftChild, node_value)
    else:
        if root_node.rightChild.data == node_value:
            print("The value is found")
        else:
            searchNode(root_node.rightChild, node_value)


def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.leftChild = deleteNode(root_node.leftChild, node_value)
    elif node_value > root_node.data:
        root_node.rightChild = deleteNode(root_node.rightChild, node_value)
    else:
        if root_node.leftChild is None:
            temp = root_node.rightChild
            root_node = None
            return temp
        
        if root_node.rightChild is None:
            temp = root_node.leftChild
            root_node = None
            return temp
        
        temp = minValueNode(root_node.rightChild)
        root_node.data = temp.data 
        root_node.rightChild = deleteNode(root_node.rightChild, temp.data)
    return root_node


def deleteBST(root_node):
    root_node.data = None
    root_node.leftChild = None
    root_node.rightChild = None
    return "Deleted"

