# Binary Tree implementation using Linked List
# Create Traverse Search Insert Delete
# Binary tree has always at most 2 children

# this module could be found in the Stack-Queue repo
import queueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data  #value
        self.left_child = None
        self.righ_child = None


def preOrderTraversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrderTraversal(root_node.left_child)
    preOrderTraversal(root_node.right_child)


def inOrderTraversal(root_node):
    if not root_node:
        return
    inOrderTraversal(root_node.left_child)
    print(root_node.data)
    inOrderTraversal(root_node.right_child)


def postOrderTraversal(root_node):
    if not root_node:
        return
    postOrderTraversal(root_node.left_child)
    postOrderTraversal(root_node.right_child)
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
            if (root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            
            if (root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)


def searchBT(root_node, nodeValue):
    if not root_node:
        return "Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            
            if (root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)
        return "Not Found"


def insertNodeBT(root_node, newNode):
    if not root_node:
        root_node = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left_child is not None:
                customQueue.enqueue(root.value.left_child)
            else:
                root.value.left_child = newNode
                return "Inserted"
            if root.value.right_child is not None:
                customQueue.enqueue(root.value.right_child)
            else:
                root.value.right_child = newNode
                return "Inserted"


def getDeepestNode(root_node):
    if not root_node:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            
            if (root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)
        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(root_node, dNode):
    if not root_node:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is dNode:
                    root.value.right_child = None
                    return
                else:
                    customQueue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is dNode:
                    root.value.left_child = None
                    return
                else:
                    customQueue.enqueue(root.value.left_child)


def deleteNodeBT(root_node, node):
    if not root_node:
        return "Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(root_node)
                root.value.data = dNode.data
                deleteDeepestNode(root_node, dNode)
                return "Deleted"
            if (root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)
            
            if (root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)
        return "Failed to delete"


def deleteBT(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "Deleted"

        
            





