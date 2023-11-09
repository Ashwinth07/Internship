class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    
    def enqueue(self,item):
        return self.items.insert(0,item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Queue is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Queue is empty")

    def size(self):
        return len(self.items)

    def display(self):
        return self.items
    
queue = Queue()
n = int(input("Enter the size of QUEUE: "))
for i in range(n):
    queue.enqueue(int(input(f"Enter the number {i}:")))

print(queue.peek())

print(queue.dequeue())

print(queue.dequeue())

print(queue.size()) 

print(queue.display())