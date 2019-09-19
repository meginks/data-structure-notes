class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 
    def __str__(self): 
        return str(self.data)


class SinglyLinkedCircularList:
    #constructor to hold our singly linked list 
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self, data): 
        node = Node(data) 
        if self.head: 
            self.head.next = node 
            self.head = node 
        else: 
            self.head = node 
            self.tail = node 
        self.head.next = self.tail #This is the only thing that differs it from a normal single linked list
        self.size += 1 
    
    def delete(self, data): 
        current = self.tail 
        prev = self.tail 
        while prev == current or prev != self.head: #we have to control for where to stop in the while loop or we'll get caught in an infinite loop
            if current.data == data: 
                if current == self.tail: 
                    self.tail = current.next 
                    self.head.next = self.tail 
                else: 
                    prev.next = current.next 
                self.size -= 1 
                return 
            prev = current 
            current = current.next 
    
    def iter(self):
        """Traverse the list -- Be careful because we'll get stuck in an infinite loop due to the circular nature of a SLCL. If you really want to use this, make sure to control with some kind of counter when you implement the method.""" 
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val  

    def search(self, data):
        """This looks for an item in the list and returns true or false""" 
        for node in self.iter():
            if data == node:
                return True
            return False

    def clear(self): 
        """ Clear the entire list. """ 
        self.tail = None 
        self.head = None 