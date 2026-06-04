class DoublyLinkedList:
    def __init__ (self, value, prev=None, next= None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = DoublyLinkedList(homepage)
        

    def visit(self, url: str) -> None:
        self.cur.next = DoublyLinkedList(url, self.cur)
        self.cur = self.cur.next
        

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.value 

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)