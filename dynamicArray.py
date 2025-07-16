class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None]*capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        capacity -= 1


    def pushback(self, n: int) -> None:
        if self.capacity <= 0:
            self.resize()
        self.array[len(self.array)-1] = n
        self.capacity -= 1


    def popback(self) -> int:
        temp = self.array[len(self.array)-1]
        self.array[self.capacity-1] = None
        self.capacity += 1
        return temp

    def resize(self) -> None:
        newArray = [None]*(self.capacity*2)

        ix = 0

        for elem in self.array:
            newArray[ix] = elem
            ix += 1
        
        self.array = newArray
        


    def getSize(self) -> int:

        size = 0

        for elem in self.array:
            if not elem is None:
                size += 1

        return size
        
    
    def getCapacity(self) -> int:

        return self.capacity
