#python2
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def find_node(self,value,node = None):
        if (self.root == None):
            return None

        if (node == None):
            node = self.root

        node_found = None

        if (node.value == value):
            node_found=node
        else:
            children = node.children
            for child in children:
                node_found=self.find_node(value,child)

        return node_found

    def build_tree(self):
        self.root = Node(1)

        child11 = Node(11)
        self.root.children.append(child11)
        child12 = Node(12)
        self.root.children.append(child12)

        child121 = Node(121)
        child12.children.append(child121)
        child122 = Node(122)
        child12.children.append(child122)


tree = Tree()
tree.build_tree()
node = tree.find_node(1)
print node.value
