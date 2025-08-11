class Deque:
    
    def __init__(self):
        self.beginning = None
        self.end = self.beginning
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        newNode = queueNode(value, self.end, None)
        if self.size == 0:
            self.beginning = newNode
            self.end = self.beginning
        else:
            self.end.behind = newNode    
            self.end = newNode
        
        self.size += 1


    def appendleft(self, value: int) -> None:
        newNode = queueNode(value, None, self.beginning)
        if self.size == 0:
            self.beginning = newNode
            self.end = self.beginning
        else:
            self.beginning.front = newNode
            self.beginning = newNode

        self.size += 1
        

    def pop(self) -> int:
        if self.size == 0:
            return -1
        temp = self.end
        self.end = self.end.front
        if self.end:
            self.end.behind = None   
        self.size -= 1
        return temp.value
    

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        temp = self.beginning
        self.beginning = self.beginning.behind
        if self.beginning:
            self.beginning.front = None
        self.size -= 1
        return temp.value

class queueNode:

    def __init__(self, value, front = None, behind = None):
        self.value = value
        self.front = front
        self.behind = behind