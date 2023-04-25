#single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self, list1): 
        self.head = None
        for i in list1:
            self.insert(i)
   
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            # find tail
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

        return newNode

    def pop_head(self):
        self.head = self.head.next
   # print method for the linked list
    def __repr__(self):
        current = self.head
        rep = ''
        while(current):
            rep += str(current.data) + '; '
            current = current.next

        return rep


list1 = LinkedList([1, 3, 4])
list2 = LinkedList([1, 2, 4])
print(list1)

print(list1.head.data)

def merge2List(list1, list2):
    if(list1 == None or list1.head == None):
        return list2
    if(list2 == None or list2.head == None):
        return list1

    lm = LinkedList([])
    x = list1.head
    y = list2.head
    if(x.data <= y.data):
        tail = lm.insert(x.data)
        list1.pop_head()
        tail.next = merge2List(list1, list2).head
    else:
        tail = lm.insert(y.data)
        list2.pop_head()
        tail.next = merge2List(list1, list2).head
    return lm

print(merge2List(list1, list2))
        
