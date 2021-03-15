# Binary Heap implementation using array
# Create Traverse Search Insert Delete
# Binary tree has always at most 2 children

# Binary Heap has root node either min value or max value
# Its also a complete tree, all levels filled completely
# Find and Insert operations O(logN), thus using array


class Heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]
        self.heap_size = 0
        self.capacity = size + 1


def peekOfHeap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]


def sizeOfHeap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size


def levelOrderTraversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size+1):
            print(root_node.custom_list[i])


def heapTreeInsert(root_node, index, heap_type):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heap_type == "Min":
        if root_node.custom_list[index] < root_node.custom_list[parentIndex]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parentIndex]
            root_node.custom_list[parentIndex] = temp
        heapifyTreeInsert(root_node, parentIndex, heap_type)
    elif heap_type == "Max":
        if root_node.custom_list[index] > root_node.custom_list[parentIndex]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parentIndex]
            root_node.custom_list[parentIndex] = temp
        heapifyTreeInsert(root_node, parentIndex, heap_type)


def insertNode(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.capacity:
        return "The Binary Heap is Full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapifyTreeInsert(root_node, root_node.heap_size, heap_type)
    return "The value has been successfully inserted"


def heapTreeExtract(root_node, index, heap_type):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < leftIndex:
        return
    elif root_node.heap_size == leftIndex:
        if heap_type == "Min":
            if root_node.custom_list[index] > root_node.custom_list[leftIndex]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[leftIndex]
                root_node.custom_list[leftIndex] = temp
            return
        else:
            if root_node.custom_list[index] < root_node.custom_list[leftIndex]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[leftIndex]
                root_node.custom_list[leftIndex] = temp
            return

    else:
        if heap_type == "Min":
            if root_node.custom_list[leftIndex] < root_node.custom_list[rightIndex]:
                swap_child = leftIndex
            else:
                swap_child = rightIndex
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        else:
            if root_node.custom_list[leftIndex] > root_node.custom_list[rightIndex]:
                swap_child = leftIndex
            else:
                swap_child = rightIndex
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
    heapifyTreeExtract(root_node, swap_child, heap_type)


def extractNode(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extractedNode = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapifyTreeExtract(root_node, 1, heap_type)
        return extractedNode
 

def deleteEntireBinaryHeap(root_node):
    root_node.custom_list = None


