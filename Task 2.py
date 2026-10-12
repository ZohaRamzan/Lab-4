class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
q=Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
print("Queue:", q.queue)
print("Removed:", q.dequeue())
print("Queue after dequeue:",q.queue)
print("Front element:", q.front())
if q.is_empty():
    print("Empty")
else:
    print("Not empty")