class Node:
    def __init__(self, key, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> Node:
        
        newNode = Node(key, val)

        if self.root == None:
            self.root = newNode
            return      
        
        curr  = self.root

        while curr:

            if key > curr.key:

                if not curr.right:
                    curr.right = newNode
                    return                    
                else:
                    curr = curr.right          

            elif key < curr.key:

                if not curr.left:
                    curr.left = newNode
                    return
                else:
                    curr = curr.left
            
            else:
                curr.val = val
                return



        

    

    def get(self, key: int) -> int:
        curr = self.root

        while curr:

            if key == curr.key:
                return curr.val
            
            if key > self.root.key:
                curr = curr.right
            else:
                curr = curr.left

        return -1
        

    def getMin(self) -> int:

        if not self.root:
            return -1
        
        curr = self.root

        while curr.left:
            curr = curr.left
            

        return curr.val

        
        


    def getMax(self) -> int:

        if not self.root:
            return -1
        
        curr = self.root

        while curr.right:
            curr = curr.right
            

        return curr.val


    def remove(self, key: int) -> None:

        self.removal(self.root, key)
        

    def removal(self, root, key):


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root, result):
        if not root:
            return
        
        self.inorderTraversal(root.left, result)
        result.append(root)
        self.inorderTraversal(root.right, result)

        return root