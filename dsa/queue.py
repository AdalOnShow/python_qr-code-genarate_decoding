class Queue:
    def __init__(self):
        self.items = []

    def _is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print(self.items)

    def insert(self, val):
        self.items.append(val)

    def delete(self):
        if self._is_empty():
            print("Queue is empty!")
        else:
            self.items.pop(0)


q1 = Queue()
q1.insert(2)
q1.insert(4)
q1.insert(8)

q1.delete()

# q1.print_queue()


#! double ended queue
class DEQueue:
    def __init__(self):
        self.items = []

    def _is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print(self.items)

    def insert_ad_front(self, val):
        self.items.insert(0, val)

    def delete_at_front(self):
        if self._is_empty():
            print("Queue is empty!")
        else:
            self.items.pop(0)

    def insert_ad_end(self, val):
        self.items.append(val)

    def delete_at_end(self):
        if self._is_empty():
            print("Queue is empty!")
        else:
            self.items.pop()


dq = DEQueue()
dq.insert_ad_end(4)
dq.insert_ad_end(8)
dq.insert_ad_front(2)
dq.delete_at_end()

dq.print_queue()
