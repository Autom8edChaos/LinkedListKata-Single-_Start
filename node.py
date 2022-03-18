from __future__ import annotations

class Node:
  
  def __init__(self, value, next: Node = None):
    self.value = value
    self.next: Node = next

  