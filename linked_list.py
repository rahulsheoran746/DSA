# Singly Linked List

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def traverse_linked_list(self, head):
#         if not head:
#             print("empty linked list")
#             return 
#         curr = head
#         while curr:
#             print(curr.value,'->', end= '')
#             curr = curr.next
#         print("None")
#         return head
    
#     def insert_at_start(self, head, newNode):
#         newNode.next = head
#         head = newNode
#         return head

#     def insert_at_end(self, head, newNode):
#         curr = head
#         while curr.next:
#             curr = curr.next
#         curr.next = newNode
#         return head
#     def insert_after_given_value(self, head, newNode, value):
#         curr = head
#         while curr:
#             if curr.value == value:
#                 newNode.next = curr.next
#                 curr.next = newNode
#                 break
#             curr = curr.next
#         return head
#     def update_given_value(self, head, target, new_value):
#         curr = head
#         while curr:
#             if curr.value == target:
#                 curr.value = new_value
#             curr = curr.next
#         return head
#     def deletefirstElement(self, head):
#         if not head:
#             print('list is already empty')
#             return None
#         if not head.next:
#             print('Only one element was present in Linked list ,Now its empty')
#             return None
#         return head.next
#     def deletelastElement(self, head):
#         if not head or not head.next:
#             return None
#         curr = head
#         while curr.next.next :
#             curr = curr.next
#         curr.next = None
#         return head
#     def deleteElementAtGivenPosition(self, head, position):
#         if position == 0:
#             return head.next
#         curr = head
#         prev = None
#         for _ in range(position):
#             prev, curr = curr, curr.next
#             if not curr:
#                 break
#         if curr:
#             prev.next = curr.next
#         return head
#     def deleteElementforGivenData(self, head, value):
#         if not head:
#             print("List is empty.")
#             return None
#         if head.value == value:
#             return head.next
#         prev = None
#         curr = head
#         while curr:
#             if curr.value == value:
#                 prev.next = curr.next
#                 break
#             prev, curr = curr, curr.next
#         else:
#             print(f"Value '{value}' not found in the list.")
#         return head
#     def length_of_linked_list(self, head):
#         if not head:
#             return 0
#         curr = head
#         length = 0
#         while curr:
#             length+=1
#             curr = curr.next
#         return length


# node1 = Node('a')
# head = node1
# node2 = Node('b')
# node1.next = node2
# node3 = Node('c')
# node2.next = node3
# node4 = Node('d')
# node3.next = node4
# print('Initial Linked list')
# head = head.traverse_linked_list(head)
# print()
# newNode = Node('1')
# print('Insertion at start:')
# head = newNode.insert_at_start(head, newNode)
# head = head.traverse_linked_list(head)
# print()
# newNode = Node('2')
# print('Insertion at end:')
# head = newNode.insert_at_end(head, newNode)
# head = head.traverse_linked_list(head)
# print()
# newNode = Node('3')
# print('Insertion after given value:')
# head = newNode.insert_after_given_value(head, newNode, 'b')
# head = head.traverse_linked_list(head)
# print()
# target = '3'
# new_value = 'e'
# print('update given value')
# head = newNode.update_given_value(head, target, new_value)
# head = head.traverse_linked_list(head)
# print()
# print('linked list after deletion from start:')
# head = node1.deletefirstElement(head) 
# head = node1.traverse_linked_list(head)
# print()
# print('linked list after deletion from end:')
# head = node1.deletelastElement(head) 
# head = node1.traverse_linked_list(head)
# print()
# print('linked list after deletion from given position:')
# position = 6
# head = node1.deleteElementAtGivenPosition(head, position) 
# head = node1.traverse_linked_list(head)
# print()
# #Delete a Linked List Node of a Given Data
# print('Delete a Linked List Node of a Given Data')
# value_to_delete = 'f'
# head = node1.deleteElementforGivenData(head, value_to_delete) 
# head = node1.traverse_linked_list(head)
# print()
# length = node1.length_of_linked_list(head)
# print('length of linked list:', length)

# # Doubly Linked List
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None
#     def traverse_doubly_linked_list(self, head):
#         if not head:
#             print('Empty Linked list')
#             return
#         curr = head
#         while curr:
#             print(curr.data,'<->',end= '')
#             curr = curr.next
#         print('None')
#     def add_element_at_start(self, head, newNode):
#         newNode.next = head
#         if head:
#             head.prev = newNode
#         return newNode
#     def add_element_at_end(self, head, newNode):
#         if not head:
#             return newNode
#         curr = head
#         while curr.next:
#             curr = curr.next
#         curr.next = newNode
#         newNode.prev = curr
#         return head
#     def add_element_after_given_node(self, node, newNode):
#         if node is None:
#             print("Error: The given node is None")
#             return
#         newNode.prev = node
#         newNode.next = node.next
#         if node.next:
#             node.next.prev = newNode
#         node.next = newNode

#     def add_element_before_given_node(self, node, newNode):
#         if node is None:
#             print("Error: The given node is None")
#             return
#         newNode.next = node
#         newNode.prev  = node.prev
#         if node.prev:
#             node.prev.next = newNode
#         node.prev = newNode
#     def delete_element_at_start(self, head):
#         if head is None:
#             print("Doubly linked list is empty")
#             return None
        
#         if head.next is None:
#             return None
#         newHead = head.next
#         newHead.prev = None
#         del head
#         return newHead
#     def delete_element_at_end(self, head):
#         if head is None:
#             print("Doubly linked list is empty")
#             return None
#         if head.next is None:
#             return None
#         curr = head
#         while curr.next.next:
#             curr = curr.next
#         del_node = curr.next
#         del del_node
#         curr.next = None
#         return head
#     def delete_element_at_given_position(self, head, position):
#         if head is None:
#             print('Doubly Linked list is empty')
#             return None
#         if position < 0:
#             print('Invalid position')
#             return head
#         if position == 0:
#             if head.next:
#                 head.next.prev = None
#             return head.next
#         curr = head
#         count = 0
#         while curr and count < position:
#             curr = curr.next
#             count += 1
#         if curr is None:
#             print("Position out of range")
#             return head
#         if curr.next:
#             curr.next.prev = curr.prev
#         if curr.prev:
#             curr.prev.next = curr.next
#         del curr
#         return head 

# node1 = Node(1)
# head = node1
# node2= Node(2)
# node1.next = node2
# node2.prev = node1
# node3 = Node(3)
# node2.next = node3
# node3.prev = node2
# print('Traversing LInked LIst:')
# node1.traverse_doubly_linked_list(head)
# newNode = Node(0)
# head = node1.add_element_at_start(head, newNode)
# print('Adding element at start of Linked List:')
# node1.traverse_doubly_linked_list(head)
# newNode = Node(4)
# head = node1.add_element_at_end(head, newNode)
# print('Adding element at end of Linked List:')
# node1.traverse_doubly_linked_list(head)
# newNode = Node(5)
# node1.add_element_after_given_node(node3, newNode)
# print('Adding element after given node of Linked List:')
# node1.traverse_doubly_linked_list(head)
# newNode = Node(6)
# node1.add_element_before_given_node(node3, newNode)
# print('Adding element before given node of Linked List:')
# node1.traverse_doubly_linked_list(head)
# head = node1.delete_element_at_start(head)
# print('Delete element at start of Linked List:')
# node1.traverse_doubly_linked_list(head)
# head = node1.delete_element_at_end(head)
# print('delete element at end of Linked List:')
# node1.traverse_doubly_linked_list(head)
# position = 4
# print('delete element at given position of Linked List: ', position)
# head = node1.delete_element_at_given_position(head, position)
# node1.traverse_doubly_linked_list(head)


# Circular LInked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def tranverse_linked_list(self):
        if  self.head  is None:
            print('Circular Linked list is empty')
            return 
        curr = self.head
        while True:
            print(curr.data, '->', end=' ')
            curr = curr.next
            if curr == self.head:
                break
        print('HEAD')

    def append_in_circular_linked_list(self, data):
        new_node  = Node(data)
        if  self.head is None:
            new_node.next = new_node
            self.head = new_node
        else :
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            self.head = new_node
            curr.next = self.head

    def insert_at_particular_position(self, position, data):
        new_node = Node(data)
        if position < 0:
            print('position is incorrect')
            return
        if position == 0:
            if self.head is None:
                new_node.next = new_node
                self.head = new_node
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                new_node.next = self.head
                self.head = new_node
                curr.next = self.head
            return
        else:
            curr = self.head
            count = 0
            while count < position -1  and curr.next != self.head:
                curr = curr.next
                count += 1
            if count != position - 1:
                print("Position out of range")
                return
            new_node.next = curr.next
            curr.next = new_node
    def delete_at_beginning(self):
        if not self.head:
            print("circular LInked list is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return 
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = self.head.next
    def delete_at_end(self):
        if not self.head:
            print("circular LInked list is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return 
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        curr.next = self.head

    def delete_at_given_position(self, position):
        if not self.head:
            print("Circular LInked list is empty")
            return
        if position < 0:
            print('POsition is incorrect')
            return
        if position  == 0:
            if self.head.next  == self.head:
                self.head = None
                return
            else:
                curr =self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            return
        curr = self.head
        count = 0
        while count < position - 1 and curr.next != self.head:
            curr = curr.next
            count += 1
        if count != position - 1 or curr.next == self.head:
            print('position  is out of range')
            return 
        curr.next = curr.next.next

circularLinkedList = CircularLinkedList()
print('Insertion in last of linked list')
circularLinkedList.append_in_circular_linked_list(1)
circularLinkedList.append_in_circular_linked_list(2)
circularLinkedList.append_in_circular_linked_list(3)
circularLinkedList.append_in_circular_linked_list(4)
circularLinkedList.tranverse_linked_list()
print('insert at beginning of list')
circularLinkedList.insert_at_beginning(0)
circularLinkedList.tranverse_linked_list()
position = 5
print('insert at particular position:', position)
circularLinkedList.insert_at_particular_position(position, 5)
circularLinkedList.tranverse_linked_list()
print('delete at beginning of list')
circularLinkedList.delete_at_beginning()
circularLinkedList.tranverse_linked_list()
print('delete at end of list')
circularLinkedList.delete_at_end()
circularLinkedList.tranverse_linked_list()
position = 4
print('delete element at given position: ', position)
circularLinkedList.delete_at_given_position(position)
circularLinkedList.tranverse_linked_list()






        
            