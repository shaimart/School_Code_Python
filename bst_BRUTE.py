class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self,root = None):
        self.root = root

    def insert(self, value):
        new_value = Node(value)
        if self.root == None:
            self.root = new_value
            self.left = None
            self.right = None
        else:
             tmp_root = self.root
             while True:
                 if new_value.value > tmp_root.value :
                     if tmp_root.right == None:
                         tmp_root.right = new_value
                         return
                     else:
                         tmp_root = tmp_root.right
                 elif new_value.value < tmp_root.value :
                     if tmp_root.left == None:
                         tmp_root.left = new_value
                         return
                     else:
                         tmp_root = tmp_root.left 
                         
                      

            

    def fromArray(self, array):
        for value in array: 
            self.insert(value)

    def search(self, value) -> bool:
        new_value = Node(value)
        self.visited_Nodes = 0
        if self.root == None:
            return False
        else:
            tmp_root = self.root
            self.visited_Nodes += 1
            while True:
                # self.visited_Nodes += 1
                if new_value.value == tmp_root.value:
                    return True
                elif new_value.value > tmp_root.value: 
                    if tmp_root.right == None:
                        break 
                    tmp_root = tmp_root.right
                    self.visited_Nodes += 1
                elif new_value.value < tmp_root.value: 
                    if tmp_root.left == None:
                        break 
                    tmp_root = tmp_root.left
                    self.visited_Nodes += 1
        return False 

    def min(self) -> None:
        self.visited_Nodes = 0
        if self.root == None:
            return None
        tmp_root = self.root
        self.visited_Nodes += 1
        while tmp_root.left:
            tmp_root = tmp_root.left
            self.visited_Nodes += 1
        return tmp_root.value 


    def max(self) -> None:
        self.visited_Nodes = 0
        if self.root == None:
            return None
        tmp_root = self.root
        self.visited_Nodes += 1
        while tmp_root.right:
            tmp_root = tmp_root.right
            self.visited_Nodes += 1
        return tmp_root.value

    def visitedNodes(self) -> int:
        return self.visited_Nodes
    


# bst1 = BinarySearchTree()

# print(bst1.search(10))
# print(bst1.visitedNodes())
# print(bst1.min())
# print(bst1.max())  


# bst2 = BinarySearchTree()
# bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

# print(bst2.search(5))
# print(bst2.visitedNodes())
# print(bst2.search(7))
# print(bst2.visitedNodes())
# print(bst2.search(6))
# print(bst2.visitedNodes())
# print(bst2.search(10))
# print(bst2.visitedNodes())
# print("MIN: " + str(bst2.min()))
# print(bst2.visitedNodes())
# print("MAX: " + str(bst2.max()))
# print(bst2.visitedNodes())

# bst3 = BinarySearchTree()
# bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

# print("MIN: " + str(bst3.min()))
# print(bst3.visitedNodes())
# print("MAX: " + str(bst3.max()))
# print(bst3.visitedNodes())