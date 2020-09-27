#python3

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQ:
    def __init__(self):
        self.nodes = []
        self.size = 0

    def is_empty(self):
        if (self.size == 0):
            return True
        return False

    def insert(self,value,priority):
        self.nodes.append(Node(value,priority))
        self.size += 1

    def get_max(self):
        max_priority = -1
        max_priority_node = None
        max_priority_idx = -1
        for i in range(0,len(self.nodes)):
            node = self.nodes[i]
            if node.priority > max_priority:
                max_priority = node.priority
                max_priority_node = node
                max_priority_idx = i
        if max_priority > 0:
            return node
        else:
            return None

    def extract_max(self):
        max_priority = -1
        max_priority_node = None
        max_priority_idx = -1
        for i in range(0,len(self.nodes)):
            node = self.nodes[i]
            if node.priority > max_priority:
                max_priority = node.priority
                max_priority_node = node
                max_priority_idx = i
        if max_priority > 0:
            self.size -= 1
            return self.nodes.pop(max_priority_idx)
        else:
            return None

    def remove(self,idx):
        if idx >= self.size:
            return None

        return self.nodes.pop(idx)

    def change_priority(self, idx, priority):
        if idx >= self.size:
            return None

        self.nodes[idx].priority = priority
        return self.nodes[idx]

if __name__ == "__main__":
    pque = PriorityQ()
    pque.insert(10, 5)
    pque.insert(10, 7)
    pque.insert(10, 4)
    pque.change_priority(2, 8)

    while not pque.is_empty():
        print pque.extract_max().priority