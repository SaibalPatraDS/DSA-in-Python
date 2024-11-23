## Linked List - Implementation

class SingleLinkedList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)
    
## Implementation of Linked List
Head = SingleLinkedList(10)
A = SingleLinkedList(20)
B = SingleLinkedList(30)
C = SingleLinkedList(40)
D = SingleLinkedList(50)

## Connecting All Nodes
Head.next = A
A.next = B
B.next = C
B.next = D

## Visualization of all Node Values
# print(Head)

curr = Head
while curr:
    print(curr.value)
    curr = curr.next
    
## Printing with visualization
"""Display Linked List"""
def display(head):
    curr = head
    linked_list = []
    while curr:
        linked_list.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(linked_list))

display(Head)


## Search For Certain values
def search(head, value):
    curr = head
    while curr:
        if value == curr.value:
            return True
        curr = curr.next
    return False

search(Head, 40)

## Doubly Linked List

class DoubleLinkedList:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.value)

## Implementation of Double Linked List

Head = DoubleLinkedList(10, next = Tail)
Tail = DoubleLinkedList(20, prev = Head)
A = DoubleLinkedList(50)
B = DoubleLinkedList(100)
print(Head, Tail)

## Displaying the Doubly Linked List
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" <-> ".join(elements))

## displaying the items
display(Head)

## Insertion of Element at the first position
def insertion_at_first_position(head, tail, value):
    new_node = DoubleLinkedList(value, next = head)
    head.prev = new_node
    return new_node, tail
        
    
## Insertion at first position
head, tail = insertion_at_first_position(Head,Tail, 1000)
display(head)

## Insertion at the End of The Linked List
def insertion_at_end_position(head, tail, value):
    new_node = DoubleLinkedList(value, prev = tail)
    tail.next = new_node
    return tail, new_node

## Insertion at the End Position
head, tail = insertion_at_end_position(Head, Tail, 5000)
display(head)