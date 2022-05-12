class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.val)


class BinarySearchTree:
    def __init__(self, data) -> None:
        self.root = Node(data)
    
    def insert(self, data):
        pass
        
    def remove(self):
        pass    
