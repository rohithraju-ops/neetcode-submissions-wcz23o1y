class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val
        
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        

    def remove(self, index: int) -> bool:

        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
            self.length -= 1
            return True
        
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        temp = prev.next        
        prev.next = temp.next   

        if temp.next is None:   
            self.tail = prev

        temp.next = None
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        temp = self.head        
        while temp:             
            result.append(temp.val)
            temp = temp.next
        return result
        
