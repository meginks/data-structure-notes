class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.right_child = None
        self.left_child = None 
 
    def __str__(self): 
        return str(self.data)
# The above is to keep the data separated from the structure of the tree itself. Why? Separation of concerns and to minimize possibility of mistakes.

class BinarySearchTree: 
    def __init__(self): 
        self.root_node = None
        
    def find_min(self): 
        """Find minimum value on the search tree. This takes O(h) where h is the height of the tree.""" 
        current = self.root_node 
        while current.left_child: 
            current = current.left_child 
        return current 
        
    def find_max(self): 
        """Find maximum value on the search tree. This takes O(h) where h is the height of the tree.""" 
        current = self.root_node 
        while current.right_child: 
            current = current.right_child 
        return current 
    
    def insert(self, data): 
        """ add a new node to the binary search tree. This takes O(h) where h is the height of the tree.""" 
        node = Node(data)
        if self.root_node is None: 
            self.root_node = node 
        else: 
            current = self.root_node 
            parent = None 
            while True: 
                parent = current 
                if node.data < current.data: 
                    current = current.left_child 
                    if current is None: 
                        parent.left_child = node 
                        return 
                else: 
                    current = current.right_child 
                    if current is None: 
                        parent.right_child = node 
                    return 

    def get_node_with_parent(self, data): 
        """This searches for the parent node of a node by the node's data and then returns that node with its parent""" 
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 
        return (parent, current) 

    def remove(self, data): 
        """removes a node. This takes O(h) where h is the height of the tree""" 
        parent, node = self.get_node_with_parent(data) 
        if parent is None and node is None:  # if the node doesn't exist, obviously you can't remove it
            return False 
        children_count = 0 # Get children count 
        if node.left_child and node.right_child: # if the node has a right and left child it has 2 children
            children_count = 2 
        elif (node.left_child is None) and (node.right_child is None): # if it doesn't have a left child or a right child, it has no children
            children_count = 0 
        else: # if it doesn't have 2 children and doesn't have zero children, it has to have 1 child (if it had more it wouldn't be a BST)
            children_count = 1 
        if children_count == 0: #if it has zero children
            if parent: 
                if parent.right_child is node: 
                    parent.right_child = None 
                else: 
                    parent.left_child = None 
            else: 
                self.root_node = None 
        elif children_count == 1: #if it has one child, delete it and make its child the child of its parent. 
            next_node = None 
            if node.left_child: 
                next_node = node.left_child 
            else: 
                next_node = node.right_child 

            if parent: 
                if parent.left_child is node: 
                    parent.left_child = next_node 
                else: 
                    parent.right_child = next_node 
            else: 
                self.root_node = next_node 
        else: #if the node has 2 children, figure out which one should be the parent and then shuffle the other nodes to make the order correct
            parent_of_leftmost_node = node 
            leftmost_node = node.right_child 
            while leftmost_node.left_child: 
                parent_of_leftmost_node = leftmost_node 
                leftmost_node = leftmost_node.left_child 
            node.data = leftmost_node.data 
            if parent_of_leftmost_node.left_child == leftmost_node: 
                parent_of_leftmost_node.left_child = leftmost_node.right_child 
            else: 
                parent_of_leftmost_node.right_child = leftmost_node.right_child 
    
    def search(self, data):
        current = self.root_node 
        while True:  
            if current is None: 
                return None
            elif current.data is data: 
                return data  
            elif current.data > data: #it has to be on the left or it wouldn't be a BST
                current = current.left_child 
            else: #if it's not on the left it has to be on the right
                current = current.right_child
    
     