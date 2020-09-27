#python2
# left <= root < right
class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def add_node(self,value,parent=None):
        node = Node(value)
        if (self.root == None):
            self.root = node
        else:
            if (parent == None):
                parent = self.root
            if node.value <= parent.value:
                if parent.left_child == None:
                    parent.left_child = node
                else:
                    self.add_node (value,parent.left_child)
            else:
                if parent.right_child == None:
                    parent.right_child = node
                else:
                    self.add_node (value,parent.right_child)

    def print_tree(self):
        if self.root == None:
            return
        self.print_tree_node(self.root,1)

    def print_tree_node (self,node,level):
        if node != None:
            print level,"==",node.value
            self.print_tree_node(node.left_child,level+1)
            self.print_tree_node(node.right_child, level+1)

tree = Tree()
tree.add_node(10)
tree.add_node(20)
tree.add_node(5)
tree.add_node(6)
tree.print_tree()