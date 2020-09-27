#python2
"""
Now an abstract link list has the following attributes
    every node in a link list points to its child
        node_id  == <4>  ___<2> ___<6> ___<1>
        child_id == <2>/    <6>/   <1>/   <-1>
    where child_id == <-1> denotes the last node.

    Operations:
        Add node to front of list => push_front(value)
        Return the front node of the list => node = top_front()
        Remove the front node of the list => node = pop_front()

        Add node to the end of the list => push_back(value)
        Return the last node of the list => node = top_back()
        Remove the last node of the list => node = pop_back()

"""
head=None
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        if (self.head == None):
            return True
        else:
            return False

    def find_node(self, value, node=None):
        # traverse the list to find the node, starting with head
        if (self.is_list_empty()):
            return None

        if node == None:
            node = self.head

        if node.value != value:
            if node.next == None:
                # Reach the last node and value still not found
                return None
            else:
                # Check next value
                return self.find_node(value, node.next)

        return node

    def remove_node(self, value, node = None, previous_node = None):
        if (self.is_list_empty()):
            return None

        if (node == None):
            node = self.head
            previous_node = None

        if node.value != value:
            if node.next == None:
                # Reach the end of the list and value not found
                return None
            else:
                # Remove next node if it matches
                return self.remove_node(value, node.next, node)
        else:
                if (previous_node == None):
                    # means we are removing the head
                    self.head = node.next
                else:
                    # Point the previous node to the next node, thus skipping this one
                    previous_node.next = node.next

        return node

    def push_front(self,value):
        node = Node(value)
        if (self.is_list_empty()):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def push_back(self,value):
        node = Node(value)
        if (self.is_list_empty()):
            self.head = node
        else:
            last_node = self.top_back()
            last_node.next = node

    def top_front(self):
        return self.head

    def top_back(self):
        if (self.is_list_empty()):
            return None

        node = self.head
        while (node.next != None):
            node = node.next
        return node

    def pop_front(self):
        node = self.top_front()
        self.head = node.next
        return node

    def pop_back(self):
        node = self.top_back()
        self.remove_node(node.value)
        return node

    def print_list(self):
        node = self.top_front()
        print "value  next.value"
        while (node != None):
            if (node.next != None):
                print node.value, node.next.value
            else:
                print node.value, None

            node = node.next


# --- test code ---
# Append to list
# Prepend to list
def populate_list_back(linked_list):
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(4)
    linked_list.push_back(6)
    linked_list.push_back(10)
    linked_list.push_back(17)
    linked_list.push_back(15)
    linked_list.push_back(16)
    linked_list.push_back(27)

def populate_list_front(linked_list):
    linked_list.push_front(100)
    linked_list.push_front(200)
    linked_list.push_front(400)
    linked_list.push_front(600)
    linked_list.push_front(1000)
    linked_list.push_front(1700)
    linked_list.push_front(1500)
    linked_list.push_front(1600)
    linked_list.push_front(2700)

def print_node(node):
    if (node == None):
        print "Empty"
    else:
        print node.value

linked_list = LinkedList()
populate_list_back(linked_list)
"""
node = linked_list.find_node(1)
print_node(node)
node = linked_list.find_node(2)
print_node(node)
node = linked_list.find_node(27)
print_node(node)

node=linked_list.pop_front()
while (node.next != None):
    node = linked_list.pop_front()

node = linked_list.find_node(1)
print_node(node)
"""

linked_list.print_list()
linked_list.remove_node(2)
print "After"
linked_list.print_list()
