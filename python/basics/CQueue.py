#python3

class Node:
    def __init__(self,value):
        self.value = value

class Queue:
    def __init__(self):
        self.size = 0
        self.nodes = []

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def push_back(self, value):
        self.enq(value)
    def enq(self,value):
        node = Node(value)
        self.nodes.append(node)
        self.size += 1

    def pop_front(self):
        return self.deq()
    def deq(self):
        if self.is_empty():
            return None

        node = self.nodes.pop(0)
        self.size -= 1
        return (node)

if __name__ == "__main__":
    que = Queue()
    que.enq(10)
    que.enq(20)

    while not que.is_empty():
        print (que.deq().value)