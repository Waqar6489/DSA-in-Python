class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        if len(self.items) == 0:
            return None
        return len(self.items)

    def peak(self):
        return self.items[-1]

    def display(self): 
        return self.items[:]                     


s= Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
print('after push list',s.display())    
print('pop element',s.pop(),s.display())
print('size element',s.size(),s.display())
print('peak element',s.peak(),s.display())

#stack LIFO
# last in first out

