from nodes import Node

class Queue:
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    
    def peek(self):
        return self.head.get_value()