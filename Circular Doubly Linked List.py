#Linked list
class Node:
    def __init__(self, data):       #Circular doubly; to implement- reverse access (another argument- path [reverse...])
        self.data = data
        self.next = self
        self.prev = self            #Doubly?; must be None if will also be used for queues...?
        
class LinkedList:
    def __init__(self):
        self.head = None            #Starts w/ no obj, so head points to null
        #Pointers indicate what Node they point to
        
    def search(self, target):       #O(n)
        """
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
        """
        
        current = self.head                         #Pointer?- object?, no tail?
        
        if self.head == None:
            return None
        
        while 1:                                    #While not 0/None
            if current.data == target:
                return current, current.data        #Returns object?
            current = current.next
            if current == self.head:
                return None

    def insert(self, node, position):       #Argument is a Node obj, O(1); 0-based position, forward-path
        """
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        node.prev = None
        """

        #Get current node before that position
        if self.head == None:
            self.head = node
        else:
            current = self.head
            for _ in range(position):           #range(x)- repeat x times
                if current.next == self.head:
                    break
                else:
                    current = current.next
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            if position == 0:
                self.head = node
    
    def delete(self, node):     #O(1)
        """
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        """
        
        if self.head == None:
            return
        if node == self.head:
            if self.head.next == self.head:
                self.head = None
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.head = node.next
                
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
    
    def display(self):
        if self.head == None:
            return "Empty list"
        
        current = self.head
        string = ""
        while 1:
            string += str(current.data) + ", "
            current = current.next
            if current == self.head:
                break
        return string
            
    #If we don't have pointer (only data), search first then delete

cdll = LinkedList()
node1, node2, node3, node4, node5, node6, node7, node8, node9, node0 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(0)
cdll.insert(node1,0)
cdll.insert(node2,0)
cdll.insert(node3,1)
cdll.insert(node4,2)
cdll.delete(node3)

#print(node5.next)
#print(node5.prev)
##print(node3.next)
#print(node3.prev)
print(cdll.display())
print(cdll.search(1))
#print(Node(3))