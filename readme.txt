In this problem, we are going to be implementing our own methods for the linked list data structure we are creating, so we should be able to create new instances of the LinkedList object. Our methods will be able to traverse the linked list as well remove or add nodes to either end of the linked list.

### The Specifics
The linked list is essentially a list of nodes, so we will have to define a Node class that our LinkedList constructor can use. We assign a node to act as the head or front of the list and we assign another node to act as the tail or back of the list.

In this case we are going to create a singly linked list, so we only need a Next and no Previous on the list.


#### The LinkedList has the following basic methods:
- **add_tail** inserts a new node on the end of the list
- **remove_tail** removes the last node of the list
- **add_head** inserts a new node at the beginning of the list
- **remove_head** removes the first node
- **add** inserts a node on a certain index
- **remove** deletes a node on a certain index
- **search** traverses the list of nodes to search for a specific node on an index.

_At the bottom, there is a graphical explanation of each method_  
#### The Node class has two properties:
- **value** which stores the value of the Node
- **next** which points to the next node in the list

#### Limitations and context: 
- a skeleton of the linked list and node is already created
- we can not use an array

### Steps:
- searching raises an IndexError in case of:
  - empty linked list
  - a not existing index (this can be implemented after add_head is fully implemented)
- adding items to the head and searching them
  - one, two, many
- removing an item from the head
  - one, two, many
- adding an item on a certain location
  - middle, front, end
- removing an item on a certain location
  - middle, front, end
- adding an item to the tail
- removing an item from the tail

## Graphical explanation of methods:

    This is how a linked list with four items can be represented:
              0      1      2      3     
    [head]   cow -> chk -> mom -> dad  [tail]
    
    >>> add_head('flem')
              0      1      2      3      4
    [head]  flem -> cow -> chk -> mom -> dad  [tail]

    >>> remove_head('flem')
              0      1      2      3      
    [head]   cow -> chk -> mom -> dad  [tail]

    >>> search(2)
    'mom'

    >>> remove(2)
              0      1      2      
    [head]   cow -> chk -> dad  [tail]

    >>> add_tail('earl')
              0      1      2      3      
    [head]   cow -> chk -> dad -> earl  [tail]

    >>> remove_tail()
              0      1      2      
    [head]   cow -> chk -> dad  [tail]
    