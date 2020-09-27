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

    def find_node(self, value):
        # traverse the list to find the node, starting with head
        if (self.is_list_empty()):
            return None

        node = self.head
        value_found = False
        while (node != None) and (value_found == False):
            if (node.value == value):
                value_found = True
            else:
                node = node.next
        if (value_found):
            return node
        else:
            return None

    def remove_node(self, value):
        if (self.is_list_empty()):
            return None

        # traverse the list to find the node, starting with head
        node = self.head
        value_found = False
        previous_node = None
        while (value_found == False) and (node != None):
            if (node.value == value):
                if (previous_node == None):
                    # means we are removing the head
                    self.head = node.next
                else:
                    # Point the previous node to the next node, thus skipping this one
                    previous_node.next = node.next

                value_found = True
            else:
                previous_node = node
                node = node.next

        if (value_found):
            return node
        else:
            return None

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


def test1():
    linked_list = LinkedList()
    populate_list_back(linked_list)

    linked_list.print_list()

def test2():
    linked_list = LinkedList()
    populate_list_front(linked_list)

    linked_list.print_list()

def test3():
    linked_list = LinkedList()
    populate_list_back(linked_list)

    while(not linked_list.is_list_empty()):
        node = linked_list.pop_back()
        print node.value

test2()
