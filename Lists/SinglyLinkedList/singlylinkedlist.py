class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 
    def __str__(self): 
        return str(self.data)


class SinglyLinkedList:
    #constructor to hold our singly linked list 
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    #THIS APPEND METHOD IS O(n) AND IS NOT VERY PERFORMANT BECAUSE IT HAS TO TRAVERSE THE ENTIRE LIST TO ADD ONE TO THE END
    # def append(self, data):
    # # Encapsulate the data in a Node
    #     node = Node(data)
    #     if self.tail == None:
    #         self.tail = node
    #     else:
    #         current = self.tail
    #         while current.next:
    #             current = current.next
    #         current.next = node 

    #THIS APPEND METHOD IS O(1) BECAUSE IT KEEPS TRACK OF WHERE THE HEAD IS AND WE ADD STUFF TO THE HEAD
    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1
    
    #example of singly linked list traversal 
    # current = animals.tail 
    # while current: 
    #     print(current.data) 
    # current = current.next
    #THIS IS A BETTER WAY TO TRAVERSE A LIST BECAUSE IT DOESN'T ALLOW THE NODES TO BE EXPOSED TO THE PROGRAMMER
    def iter(self):
        """Traverse the list""" 
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val  
            
    def delete(self, data): 
        """Deletes a node by the data inside of it. O(n) because you must traverse the whole list to find the one to delete.""" 
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next 

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

    #THIS SIZE METHOD IS O(n) BECAUSE IT REQUIRES YOU TO TRAVERSE THE ENTIRE LIST TO SEE HOW BIG IT IS, adding a size attribute and putting it on the append method changed our runtime from O(n) to O(1)
    # def size(self):
    #     count = 0
    #     current = self.tail
    #     while current:
    #         count += 1
    #         current = current.next
    #     return count 


#example of instantiation of singly linked list  
animals = SinglyLinkedList() 
animals.append('cat')
animals.append('dog')
animals.append('rabbit')
animals.append('giraffe')

# call the iter method to print each item in the singly linked list 
for animal in animals.iter(): 
    print(animal) 

# call the delete method to delete one of the nodes 
animals.delete('dog') 

for animal in animals.iter():
    print(animal)