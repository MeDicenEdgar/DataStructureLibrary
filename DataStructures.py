#-----------------------------Linked List-------------------------------------
class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self, data):
        new = LLNode(data)
        new.next = self.head
        self.head = new

    def insert(self, previous, data):
        if type(previous) == LLNode:
            new = LLNode(data)
            new.next = previous.next
            previous.next = new 
        else:
            print("Previous is not a valid Node")
            return
    def deleteData(self, data):
        temp = self.head
        if temp is not None:
            if temp.value==data:
                self.head = temp.next
                temp = None
                return
                
        while temp is not None:
            if temp.value == data:
                prev.next = temp.next
                temp = None
                return
            prev = temp    
            temp = temp.next
        
    def deleteIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(index):
            prev = temp
            temp = temp.next
            if temp == None:
                print("That index is empty")
                return
        prev.next=temp.next
        temp = None
    
    def deleteList(self):
        temp = self.head
        while temp is not None:
            next = temp.next
            del temp.value
            temp = next

    def printList(self):
        wow = self.head
        while wow:
            print(wow.value)
            wow = wow.next

#-----------------------------Stack-------------------------------------------
class Stack:
    def __init__(self, elements = []):
        self.elements = elements

    def append(self, element):
        self.elements.append(element)
    
    def pop(self):
        return self.elements.pop()

    def len(self):
        return len(self.elements)
    
    def empty(self):
        if len(self.elements)== 0:
            return True
        else:
            return False
    def peek(self):
        return self.elements[-1]

#-----------------------------Queue-------------------------------------------
class Queue:
    def __init__(self, elements = []):
        self.elements = elements

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.pop(0)

    def front(self):
        return self.elements[0]

    def back(self):
        return self.elements[-1]

#-----------------------------Binary Tree-------------------------------------
class BTNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root