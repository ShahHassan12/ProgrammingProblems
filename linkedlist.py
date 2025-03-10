class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self) -> None:
        '''
        '''
        self.head = None
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        :type index: int
        :rtype int       
        """

        if index < 0 or index >= self.size or self.size <= 0:
            return -1

        i = 0
        curr = self.head

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

    
    def insertHead(self, val: int) -> None:
        """
        :type: int
        :rtype: None
        """
        if self.size <= 0:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            self.head = Node(val, next = self.head)
            self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size <= 0:
            self.insertHead(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size or self.size <= 0:
            return False
        
        if index == 0:
            temp = self.head      
            self.head = self.head.next
            del temp
            
            self.size -= 1
            return True            
        
        i = 0
        curr = self.head

        while curr:  

            if i == index:                
                temp = curr.next
                curr.next = None
                prev.next = temp
                if index == self.size - 1:
                    self.tail = prev
                self.size -= 1
                return True
            
            
            prev = curr
            curr = curr.next
            i +=1

    
    def getValues(self) -> list[int]:
        values = []
        
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
            