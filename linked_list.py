from out_of_bound_error import OutOfBoundError
from node import Node

class LinkedList:
  
  def __init__(self):
    self.item = None

  def add_tail(self, item):
    pass

  def add_head(self, item):
    if self.item is None:
      self.item = Node(item,None)
    else:
      olditem = self.item
      self.item = Node(item, olditem)

  def add(self, index, item):
    pass

  def delete(self, index):
    pass
  
  def delete_tail(self):
    pass

  def delete_head(self):
    pass
 
  def search(self, index: int) -> object:
    if index > 0 and self.item.next is None:
      raise OutOfBoundError

    found_item = self.item
    for i in range(index):
      found_item = self.item.next
    if found_item is None:
      raise RuntimeError
    return found_item.value
    