class Queue:
    def __init__(self):
        self.itmes = []

    def _is_empty(self):
        return len(self.itmes) == 0

    def print_queue(self):
        print(self.itmes)

    def insert(self, val):
        self.itmes.append(val)

    def delete(self):
        if self._is_empty():
            print("Queue is empty!")
        else:
            self.itmes.pop(0)


q1 = Queue()
q1.insert(2)
q1.insert(4)
q1.insert(8)

q1.delete()

q1.print_queue()
