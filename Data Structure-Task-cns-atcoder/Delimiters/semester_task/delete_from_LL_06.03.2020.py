# n = int(input())
# ll = []
# for i in range(n):
#     ele = int(input())
#     ll.append(ele)
# position = int(input())
# def deleteNode(ll,pos):
#     ll.pop(pos)
#     return ll
# new_ll = deleteNode(ll,position)
# for i in new_ll:
#     print(i, end = " ")
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Appends a new node at the end.  This method is
    # defined inside LinkedList class shown above */
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # Utility function to print the linked list

    def deleteNode(self, position):

        # If linked list is empty
        if self.head == None:
            return

            # Store head node
        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

            # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

            # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

ll = LinkedList()
n = int(input())
for i in range(n):
    ele = int(input())
    ll.append(ele)
position = int(input())
ll.deleteNode(position)
ll.printList()
