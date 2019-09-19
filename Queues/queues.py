class ListQueue: 
    def __init__(self): 
        self.items = [] 
        self.size = 0 

    def enqueue(self, data):
        """add items to the queue. Note that this is not efficient for large lists."""  
        self.items.insert(0, data) #note that we could also use .shift() here -- the point is to add the new thing at index 0 to mimic a queue
        self.size += 1 
    
    def dequeue(self):
        """removes an item from the queue"""
        data = self.items.pop()
        self.size -= 1
        return data 


class StackBasedQueue: 
    """this is a stack-based queue""" 
    def __init__(self): 
        self.inbound_stack = [] 
        self.outbound_stack = [] 

    def enqueue(self, data): 
        """adds item to the incoming stack"""
        self.inbound_stack.append(data) 
    
    def dequeue(self, data): 
        if not self.outbound_stack: 
            while self.inbound_stack: 
                self.outbound_stack.append(self.inbound_stack.pop()) 
        return self.outbound_stack.pop() 

class Node: 
    def __init__(self, data=None, next=None, prev=None): 
        self.data = data 
        self.next = None 
        self.prev = None
    def __str__(self): 
        return str(self.data)

class NodeBasedQueue:
    """a doubly linked list that behaves like a queue""" 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.count = 0 

    def enqueue(self, data): 
        new_node = Node(data, None, None) 
        if self.head is None: 
            self.head = new_node 
            self.tail = self.head 
        else: 
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
        self.count += 1 
    
    def dequeue(self): 
        # current = self.head -- book example included this line, but I don't really understand why because it doesn't matter?
        if self.count == 1: 
            self.count -= 1 
            self.head = None 
            self.tail = None 
        elif self.count > 1: 
            self.head = self.head.next 
            self.head.prev = None 
            self.count -= 1 
    
    