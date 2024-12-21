class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    reversed_string = ''
    stack = Stack()

    for char in my_string:
        stack.push(char)
    
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

print(reverse_string('Software'))