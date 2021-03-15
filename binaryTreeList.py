# Binary Tree implementation using List
# Create Traverse Search Insert Delete
# Binary tree has always at most 2 children
# Creating is O(n), rest is O(1)
# Linked list Insert is O(n) but also spcae complexity is O(n)

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.last_used_index = 0
        self.capacity = size


    def insertNode(self, value):
        if self.last_used_index + 1 == self.capacity:
            return "Binary Tree is full"
        self.custom_list[self.last_used_index+1] = value
        self.last_used_index += 1
        return "Inserted"


    def searchNode(self, nodeValue):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == nodeValue:
                return "Success"
        return "Not found"


    def preOrderTraversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)


    def inOrderTraversal(self, index):
        if index > self.last_used_index:
            return
        self.inOrderTraversal(index*2)
        print(self.custom_list[index])
        self.inOrderTraversal(index*2+1)


    def postOrderTraversal(self, index):
        if index > self.last_used_index:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.custom_list[index])


    def levelOrderTraversal(self, index):
        for i in range(index, self.last_used_index+1):
            print(self.custom_list[i])


    def deleteNode(self, value):
        if self.last_used_index == 0:
            return "There is not any node to delete"
        for i in range(1, self.last_used_index+1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "Deleted"


    def deleteBinaryTree(self):
       self.custom_list = None
       return "Deleted"



