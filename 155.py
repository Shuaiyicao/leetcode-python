class MinStack:
    def __init__(self):
        self.a = []
        self.b = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.a.append(x)
        if len(self.b) == 0 or self.b[-1] >= x:
            self.b.append(x)
    
    # @return nothing
    def pop(self):
        tmp = self.a.pop()
        if self.b[-1] == tmp:
            self.b.pop()

    # @return an integer
    def top(self):
        return self.a[-1]
        
    # @return an integer
    def getMin(self):
        return self.b[-1]