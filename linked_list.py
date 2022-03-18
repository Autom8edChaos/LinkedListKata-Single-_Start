from node import Node

class LinkedList:
  
  def __init__(self):
    self.head = None
    
  def add_tail(self, item):
    pass

  def add_head(self, item):
    self.head = Node(item, self.head)

  def delete(self, index):
    pass
  
  def delete_tail(self):
    pass

  def delete_head(self):
    pass
 
  def search(self, index: int) -> object:
    node = self.head
    for i in range(index):
      node = node.next
    
    if node:
      return node.value
    
    raise IndexError