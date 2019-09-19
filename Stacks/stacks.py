#Here is an example of function calls implementing a stack structure
def b(): 
    print('b') 
def a(): 
    b() 
a() 
print("done") 


class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 
        self.top = None 
        self.size = 0 
    
    def push(self, data): 
        """adds a new item to the top of the stack. This is O(1)""" 
        node = Node(data) 
        if self.top: 
           node.next = self.top 
           self.top = node                 
        else: 
           self.top = node 
        self.size += 1 

    def pop(self): 
        """removes an item from the top of the stack. This is O(1)""" 
        if self.top: 
            data = self.top.data 
            self.size -= 1  
            if self.top.next: 
                self.top = self.top.next 
            else: 
                self.top = None 
            return data 
        else: 
            return None 
    
    def peek(self): 
        """allows us to look at the top of the stack without changing anything on the stack""" 
        if self.top: 
            return self.top.data 
        else: 
            return None 
        
