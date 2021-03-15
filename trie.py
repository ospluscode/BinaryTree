# Trie Data Strcuture implementation with Linked list
# Trie is mainly used with Storing and Searching Strings
# Properties: any node can store multi chars, every node have links and tracks end of the string
# Create Insert Delete Search


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = Node()

    # diff insertion cases
    def insertString(self, word):
        current_node = self.root
        for i in word:
            ch = i
            node = current_node.children.get(ch)
            if node == None:
                node = Node()
                current_node.children.update({ch:node})
            current_node = node
        current_node.end_of_string = True
        print("Inserted")


    # diff search cases
    def searchString(self, word):
        current_node = self.root
        for i in word:
            node = current_node.children.get(i)
            if node == None:
                return False
            current_node = node

        if current_node.end_of_string == True:
            return True
        else:
            return False
        

    # diff search cases
    def deleteString(root, word, index):
        ch = word[index]
        current_node = root.children.get(ch)
        canThisNodeBeDeleted = False

        if len(current_node.children) > 1:
            deleteString(current_node, word, index+1)
            return False

        if index == len(word) - 1:
            if len(current_node.children) >= 1:
                current_node.end_of_string = False
                return False
            else:
                root.children.pop(ch)
                return True

        if current_node.end_of_string == True:
            deleteString(current_node, word, index+1)
            return False

        canThisNodeBeDeleted = deleteString(current_node, word, index+1)
        if canThisNodeBeDeleted == True:
            root.children.pop(ch)
            return True
        else:
            return False