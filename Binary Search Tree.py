class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        #self.parent                #No need?

class BinarySearchTree:
    def __init__(self):
        self.root = None                    #Root describes the tree (since all other nodes are connected...), like head in linked lists
        
    def isEmpty(self):
        if self.root == None:
            return True
        return False
    
    def insert(self, node):                 #To call self.root once
        if self.isEmpty():
            self.root = node
        else:
            self.insertHelper(node, self.root)
    
    def insertHelper(self, node, root):     #Put initial value to root- None?
        #Recursive- used almost always for trees
        #Can be implemented w/o recursion- loops?
        """
        if root == None:                    #For initial call
            root = self.root
        
        if root == None:                    #To see if self.root is None, base case?
            self.root = node
            return self.root                #Must return something due to recursive nature
        """             
        
        if node.data <= root.data:
            if root.left == None:
                root.left = node
                #return                      #Return if already added (if find space to add)
            else:
                self.insertHelper(node, root.left)
        else:
            if root.right == None:
                root.right = node
                #return
            else:
                self.insertHelper(node, root.right)
        return
    
    def display(self):
        array = []
        self.displayHelper(self.root, array)
        return array
    
    def displayHelper(self, root, array):
        #if root == None:
        #    return "Empty tree"
        
        #Inorder- non-descending order
        if root != None:
            self.displayHelper(root.left, array)
            array.append(root.data)
            self.displayHelper(root.right, array)
        #return
    
    def search(self, node, root):       #Needs root since recursive
        if root == None:
            data = None
        elif node.data == root.data:
            return root
        elif node.data < root.data:
            data = self.search(node, root.left)
        else:
            data = self.search(node, root.right)
        return data
    
    #def isLeaf(self, node):   
    
    def getParent(self, node, root):
        """    
        elif root.left.data == node.data or root.right.data == node.data:
            return root
        else:
            if node.data < root.data:
                parent = self.getParent(node, root.left)
            else:
                parent = self.getParent(node, root.right)
        return parent
        """
        
        if root == None:
            return None
        elif root.data == node.data:        #If node == root of main tree- handled on delete
            return "the_root"
        
        elif node.data < root.data:         #Similar cases dpt sa ibang if...
            # if root.left is None:
            #     return None
            if root.left.data == node.data:
                return root
            return self.getParent(node, root.left)
        else:
            # if root.right is None:
            #     return None
            if root.right.data == node.data:
                return root
            return self.getParent(node, root.right)
    
    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current      #Leftmost of right subtree?
    
    def delete(self, node):
        #Must note that after deleting, BST must still satisfy its properties...
        #3 cases- a leaf, node w/ 1 child, node w/ 2 children
        #Returns the node we wanna delete
        #To test/think- tree w/ height 2...
        
        #Search, recursive
        """
        if root == None:
            return root         #Usually if after return case since pag napunta rito, d n magtuloy...
        elif node.data < root.data:
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
            
        return root
        #Return pointer to root node since root may change after deletion
        """
        
        #Search
        #Return root?
        if self.isEmpty():
            return None
        
        node_temp = self.search(node, self.root)
        if node_temp == None:       #Not in tree
            return self.root
        
        #If root
        if node.data == self.root.data:
            #Case1
            if self.root.left == None and self.root.right == None:
                self.root.data = None
                self.root = None
                return self.root

            #Case2
            elif self.root.left == None and self.root.right != None:
                self.root = self.root.right
                return self.root
            elif self.root.right == None and self.root.left != None:
                self.root = self.root.left
                return self.root
                
            #Case3
            else:
                min_right = self.findMin(self.root.right)        #1/2 children, no leftchild
                parent_min_right = self.getParent(min_right, self.root)
            
                #Process min_right
                if min_right.left == None and min_right.right == None:
                    if parent_min_right.left == min_right:
                        parent_min_right.left = None
                    else:
                        parent_min_right.right = None
                    
                else:       #1 right child
                    if parent_min_right.left == min_right:
                        parent_min_right.left = min_right.right
                    else:
                        parent_min_right.right = min_right.right
                        
                self.root.data = min_right.data
                return self.root
        
        else:
            parent = self.getParent(node, self.root)   
            #Case1
            if node.left == None and node.right == None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                return self.root
            
            #Case2
            elif node.left == None and node.right != None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return self.root
                    
            elif node.right == None and node.left != None:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return self.root
            
            #Case3
            else:
                min_right = self.findMin(node.right)        #1/2 children, no leftchild
                parent_min_right = self.getParent(min_right, self.root)
                
                #Process min_right
                if min_right.left == None and min_right.right == None:
                    if parent_min_right.left == min_right:
                        parent_min_right.left = None
                    else:
                        parent_min_right.right = None
                    
                else:       #1 right child
                    if parent_min_right.left == min_right:
                        parent_min_right.left = min_right.right
                    else:
                        parent_min_right.right = min_right.right
                        
                node.data = min_right.data
                return self.root
        
        #Notes- handle if root will be deleted, can also return the node    
        #Case- root has no left or no right        
        
    def find_sum(self, root):   #At most O(2n) = O(n)
        #sum = 0
        if root == None:        #Check this
            return 0
        else:
            return root.data + self.find_sum(self, root.left) + self.find_sum(self, root.right)
    
    #Harder problem- call the tree then return the number of non-empty universal value trees
    
    
### Main ###
node1, node2, node3, node4, node5, node6, node7, node8, node9, node0 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(0)
node1_1, node2_1, node3_1 = Node(1), Node(2), Node(3)
tree = BinarySearchTree()
print(tree.isEmpty())
# tree.insert(node3)
# tree.insert(node2)
# tree.insert(node1)
# tree.insert(node5)
# tree.insert(node6)
# tree.insert(node0)
# tree.insert(node4)
# tree.insert(node7)
# tree.insert(node8)
# tree.insert(node3_1)
# tree.insert(node2_1)
# tree.insert(node1_1)

tree.insert(node3)
tree.insert(node1)
tree.insert(node5)
tree.insert(node0)
tree.insert(node2)
tree.insert(node6)
tree.insert(node4)
tree.delete(node3)
# tree.delete(node4)
# tree.delete(node5)
# tree.delete(node5)
# tree.delete(node6)
# tree.delete(node0)

# tree.insert(node3_1)
# tree.insert(node2_1)

#Care sa paginsert, mag max recurs depth exceeded pag same obj... (address?)
# tree.delete(node0)
# tree.delete(node2)
# tree.delete(node3_1)
# tree.delete(node2_1)
# tree.delete(node1)
# tree.delete(node6)

# tree.insert(node0)
# tree.insert(node1)
# tree.insert(node2)
# tree.insert(node3)
# tree.delete(node0)
# tree.delete(node2)
# tree.delete(node1)
# tree.delete(node3)
# tree.delete(node3_1)

print(tree.isEmpty())
print(tree.display())
#print(tree.root.data)       #Pweds din ito nlng isama sa call...
print(tree.search(node1, tree.root).data)

#tree.delete(node1, tree.root)
#tree.delete(node2, tree.root)
#tree.delete(node3, tree.root)
#tree.delete(node3_1, tree.root)
#print(tree.display())

#print(tree.getParent(node0, tree.root))
#x = tree.findMin(node1)
#print(tree.getParent(x, tree.root).data)