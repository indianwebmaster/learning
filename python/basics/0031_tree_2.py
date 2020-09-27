#python2
class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def add_node(self,value,parent=None):
        node = Node(value)
        if (parent == None):
            if (self.root == None):
                node.parent = None
                self.root = node
            else:
                # Root already present. Cannot replace the root in this way
                print "Cannot replace root with ",value," in this method"
                return None
        else:
            node.parent = parent
            parent.children.append(node)

        return node

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
                if (node_found==None):
                    node_found=self.find_node(value,child)

        return node_found

    def max_height(self, node=None, height=None):
        if (self.root == None):
            return 0
        if (node == None):
            node = self.root
            height = 1

        if (len(node.children) > 0):
            height += 1

        max_height = height
        for child in node.children:
            max_height = max(max_height, self.max_height(child, height))

        return max_height

    def remove_node(self,value):
        if (self.root == None):
            return None

        node = self.find_node(value)
        if (node == None):
            return None

        if len(node.children) > 0:
            print "Only a leaf can be removed"
            return None

        parent = node.parent
        if (parent == None):
            # Means we are removing the root, the only node in the tree
            self.root = None
        else:
            parent.children.remove(node)

    def print_tree(self,node=None,level=None):
        if (self.root == None):
            return None

        if (node == None):
            node=self.root
            level=1

        print "level ", level,"===", node.value

        if len(node.children) == 0:
            return None
        else:
            level += 1
            for child in node.children:
                self.print_tree(child,level)

def build_tree_1(tree):
    root = tree.add_node(1)

    child11 = tree.add_node(11,root)
    child12 = tree.add_node(12,root)

    child111 = tree.add_node(111,child11)
    child1111 = tree.add_node(1111,child111)
    child1112 = tree.add_node(1112, child111)

    child121 = tree.add_node(121,child12)
    child122 = tree.add_node(122,child12)


tree = Tree()
build_tree_1(tree)

#node = tree.find_node(122)
#print node.value

#print tree.max_height()
#tree.remove_node(121)
#tree.remove_node(122)
#print tree.max_height()

tree.print_tree()