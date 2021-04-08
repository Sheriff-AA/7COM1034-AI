class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queues:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value:
            if len(value) == 1:
                self.enqueue(value[0])
                return
            self.length = len(value)
            first_val, last_val = value.pop(0), value.pop(len(value) - 1)
            self.head = Node(first_val)
            self.tail = Node(last_val)
            current_node = self.head
            x = 0
            while x < len(value):
                current_node.next = Node(value[x])
                current_node = current_node.next
                x += 1
            current_node.next = self.tail
            return

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return "Queue is empty"
        if self.head == self.tail:
            self.tail = None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.value

    def empty(self):
        if self.length:
            return False
        return True


queue = Queues([1])
# queue.enqueue("Sheriff")
# queue.enqueue("Blessing")
# queue.enqueue("Emmanuel")
# queue.enqueue("Nitti")
# queue.enqueue("Sam")
# queue.enqueue("Khadijah")
# queue.enqueue("Riley")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.empty())
print(queue.head, queue.tail)
