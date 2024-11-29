class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None        #is instead of == for None
    
    def search(self, node):     #Similar to classic BST
        if self.isEmpty():
            return None
        
        current = self.root
        while current is not None:
            if current.data == node.data:
                return current
            elif node.data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def insert(self, node):
        if self.isEmpty():
            self.root = node
        else:
            self.insertHelper(node, self.root)
    
    def insertHelper(self, node, root):
        #Insert as leaf first
        if root is None:      #Base case
            root = node
            return root
        
        if node.data <= root.data:
            root.left = self.insertHelper(node, root.left)
        else:
            root.right = self.insertHelper(node, root.right)
        
        #root.height = 1 + max(root.left.height, root.right.height)      #Might not handle None correctly?
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        #Do the rotation here to instantly do it whenever the tree/subtrees are unbalanced
        bal_fac = self.getBalFac(root)
        
        #4cases
        if bal_fac > 1 and node.data <= root.left.data:          #Left-heavy
            return self.right_rotate(root)
        elif bal_fac < -1 and node.data > root.right.data:      #Right-heavy
            return self.left_rotate(root)
        
        elif bal_fac > 1 and node.data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        elif bal_fac < -1 and node.data <= root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        else:
            return root     #Since we changed the root?, for upper insertHelper() calls?
        
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height
    
    def getBalFac(self, root):
        if root is None:
            return 0        #Balanced
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def left_rotate(self, root):
        #Initiate
        new_root = root.right
        to_swap = new_root.left
        
        new_root.left = root
        root.right = to_swap
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))
        
        return new_root
    
    def right_rotate(self, root):
        new_root = root.left
        to_swap = new_root.right
        
        new_root.right = root
        root.left = to_swap
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        new_root.height = 1 + max(self.getHeight(new_root.left), self.getHeight(new_root.right))
        
        return new_root
    
    def display(self, root):
        if root is None:        #Base case
            return None
        else:
            left = self.display(root.left)
            right = self.display(root.right)
        return [root.data, left, right]
    
    def delete(self, node, root):       #No root deletion case yet
        #Just normal BST deletion, then rebalance
        if root == None:
            return root         #Usually if after return case since pag napunta rito, d n magtuloy...
        
        if node.data < root.data:
            root.left = self.delete(node, root.left)
        elif node.data > root.data:
            root.right = self.delete(node, root.right)
        else:
            #Case1
            if root.left == None and root.right == None:
                root = None     #If returned, either previous root.left or root.right will be None, how to terminate?
                return root
            #Case2
            elif root.left == None:
                root = root.right
                return root
            elif root.right == None:
                root = root.left
                return root
            #Case3
            else:
                #Find inorder successor of node, min of right subtree
                temp = self.findMin(root.right)
                root.data = temp.data
                root.right = self.delete(temp, root.right)
                
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        bal_fac = self.getBalFac(root)
        
        #4cases
        if bal_fac > 1 and self.getBalFac(root.left) >= 0:
            return self.right_rotate(root)
        elif bal_fac < -1 and self.getBalFac(root.right) <= 0:
            return self.left_rotate(root)
        
        elif bal_fac > 1 and self.getBalFac(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        elif bal_fac < -1 and self.getBalFac(root.left) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        else:
            return root
                
    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current      #Leftmost of right subtree?
    
class RedBlackTree:
    def __init__(self):
        self.root = None
        

### Main ###
node1, node2, node3, node4, node5, node6, node7, node8, node9, node0 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(0)
node1_1, node2_1, node3_1 = Node(1), Node(2), Node(3)

avl = AVLTree()
print(avl.isEmpty())
#avl.insert(node3)
#avl.insert(node3_1)
avl.insert(node5)
avl.insert(node3)
avl.insert(node7)
avl.insert(node2)
avl.insert(node4)
avl.insert(node6)
avl.insert(node8)
avl.delete(node8, avl.root)

print(avl.display(avl.root))


### Binary Tree Array ###
#Approach 1
array1 = []
for i in range(100):
    array1.append(None)

"""
def bst_array1_insert(array, data):
    if len(array) == 0:
        array.append([data, -1, -1])
    else:
        current_idx = 0
        free_idx = 0
        for idx in range(len(array)):
            if array[idx] == None:
                free_idx = idx
                break
        
        while array[current_idx] != None:
            array[free_idx] = [data, -1, -1]
            if data <= array[current_idx][0]:
                array[current_idx][1] = free_idx
            else:
                array[current_idx][2] = free_idx
                
            current_idx = free_idx
    
    return array
"""

def bst_array1_insert(array, data):
    if len(array) == 0:
        array.append([data, -1, -1])
    else:
        current_idx = 0
        while True:
            if data <= array[current_idx][0]:
                left_child_idx = array[current_idx][1]
                if left_child_idx == -1:
                    left_child_idx = len(array)
                    array[current_idx][1] = left_child_idx
                    array.append([data, -1, -1])
                    break
                current_idx = left_child_idx
            else:
                right_child_idx = array[current_idx][2]
                if right_child_idx == -1:
                    right_child_idx = len(array)
                    array[current_idx][2] = right_child_idx
                    array.append([data, -1, -1])
                    break
                current_idx = right_child_idx

    return array