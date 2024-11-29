class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Deque:                    #Like vector...?
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head is None
    
    def insertLeft(self, node):     #From left
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def insertRight(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def popLeft(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                self.head.next.prev = None
                self.head = self.head.next
                temp.next = None
            return data
    
    def popRight(self):
        if self.isEmpty():
            return None
        else:
            data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.tail
                self.tail.prev.next = None
                self.tail = self.tail.prev
                temp.prev = None
            return data
    
    def display(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            string = ""
            current = self.head
            while 1:
                string += str(current.data) + ", "
                if current == self.tail:
                    break
                current = current.next
            return string

class Queue:                    #Add size()?, can be implemented w/ (dynamic) arrays too
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head is None
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    
    def enqueue(self, node):
        #Add to tail
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def dequeue(self):
        #Remove from head
        #Pabaliktad ung arrows else d makadelete
        if self.isEmpty():
            return
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                self.head = self.head.next
                temp.next = None
                
    def display(self):              #Leftmost is head
        if self.isEmpty():
            return "Empty Queue"
        else:
            string = ""
            current = self.head
            while 1:
                string += str(current.data) + ", "
                if current == self.tail:
                    break
                current = current.next
            return string

class Stack:                #Baliktad parin ung arrows
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data
    
    def push(self, node):
        if self.isEmpty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):          #Returns the data too
        if self.isEmpty():
            return None
        else:
            data = self.top.data
            if self.top.next == None:
                self.top = None
            else:
                temp = self.top
                self.top = self.top.next
                temp.next = None
            return data
            
    def display(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            string = ""
            current = self.top
            while 1:
                string += str(current.data) + ", "
                if current.next == None:
                    break
                current = current.next
            return string

class Stack_Array():
    def __init__(self):
        self.array = []
    
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        return False
    
    def peek(self):
        return self.array[0]
    
    def push(self, node):
        self.array.append(node)
        
    def pop(self):
        return self.array.pop().data
    
    def display(self):
        stack = []
        for i in self.array:
            stack.append(i.data)
        return stack
    
class Queue_Array():
    def __init__(self):
        self.array = []
        #self.head_idx = 0
    
    def isEmpty(self):
        if len(self.array) == 0:
            return True
        return False
    
    def peek(self):
        return self.array[0]
    
    def enqueue(self, node):
        self.array.append(node)
        
    def dequeue(self):
        if self.isEmpty():
            return
        self.array.pop(0)
    
    def display(self):
        stack = []
        for i in self.array:
            stack.append(i.data)
        return stack


### Main ###
node1, node2, node3, node4, node5, node6, node7, node8, node9, node0 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(0)
"""
q1 = Queue()
print(q1.isEmpty())
q1.enqueue(node1)
q1.enqueue(node2)
q1.enqueue(node3)

print(q1.peek())
q1.dequeue()
print(q1.peek())
q1.enqueue(node4)
print(q1.peek())

print(q1.display())
q1.dequeue()
q1.dequeue()
print(q1.isEmpty())
"""
"""
s1 = Stack()
print(s1.isEmpty())
s1.push(node1)
s1.push(node2)
s1.push(node3)
print(s1.display())
print(s1.peek())
print(s1.pop())
print(s1.pop())
print(s1.peek())

s1.push(node4)
print(s1.peek())
print(s1.display())
print(s1.pop())
print(s1.peek())
print(s1.isEmpty())
print(s1.pop())
print(s1.isEmpty())
print(s1.pop())
print(s1.isEmpty())
print(s1.display())
"""

"""
d1 = Deque()
print(d1.isEmpty())
print(d1.display())
d1.insertLeft(node1)
d1.insertLeft(node2)
d1.insertRight(node3)
d1.insertLeft(node4)
d1.insertRight(node5)
print(d1.display())
print(d1.popLeft())
print(d1.popLeft())
print(d1.popRight())
print(d1.popRight())
"""

"""
s2 = Stack_Array()
print(s2.isEmpty())
print(s2.display())
s2.push(node1)
s2.push(node2)
print(s2.pop())
print(s2.pop())
s2.push(node7)
s2.push(node8)
s2.push(node9)
print(s2.pop())
print(s2.display())
print(s2.isEmpty())
"""

q2 = Queue_Array()
print(q2.isEmpty())
q2.enqueue(node1)
q2.enqueue(node2)
q2.enqueue(node3)
print(q2.display())
q2.dequeue()
q2.dequeue()
q2.enqueue(node7)
q2.enqueue(node8)
q2.dequeue()
print(q2.display())