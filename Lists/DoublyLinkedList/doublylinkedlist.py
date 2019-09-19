class Node(object): 
    def __init__(self, data=None, next=None, prev=None): 
        self.data = data 
        self.next = next 
        self.prev = prev 

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data): 
        """ Append an item to the list. This is O(1) """ 
        new_node = Node(data, None, None) 
        if self.head is None: #executed if the list is empty 
            self.head = new_node 
            self.tail = self.head #in this list, the tail is where new nodes get added
        else: #executed if the list isn't empty 
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
            self.count += 1 

    def delete(self, data): 
        """Deletes a node from the doubly linked list. This is O(N)""" 
        current = self.head 
        deleted_node = False 
        if current is None: #if the list has no nodes, obviously it can't delete the thing you're trying to delete
            deleted_node = False
        elif current.data == data: #if the thing you want to delete is on current (i.e. the head in this case), then delete it 
            self.head = current.next 
            self.head.prev = None 
            deleted_node = True
        elif self.tail.data == data: #if the node you want to delete is on the tail, delete it
            self.tail = self.tail.prev 
            self.tail.next = None 
            deleted_node = True
        else: # if the node you want to delete isn't on the head or tail, loop through the list until you find it, if you find it delete it, otherwise return False
            while current: 
                if current.data == data: 
                    current.prev.next = current.next 
                    current.next.prev = current.prev 
                    deleted_node = True 
                current = current.next
        if deleted_node: #decrease count by one if you deleted the node
            self.count -= 1   

    def iter(self):
        """Traverse the list""" 
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val 

    def contain(self, data): 
        """Check if the list contains an item""" 
        for node_data in self.iter(): 
            if data == node_data: 
                return True 
            return False 