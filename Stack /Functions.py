class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is Empty")
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
stack = Stack()
n = int(input("Enter the size of stack: "))
for i in range(n):
    stack.push(int(input(f"Enter the number {i}:")))
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.display())
