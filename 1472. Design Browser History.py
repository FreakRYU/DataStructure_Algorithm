class ListNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage):
        self.head = self.current = ListNode(value = homepage)

    def visit(self, url):
        self.current.next = ListNode(value = url, prev = self.current)
        self.current = self.current.next

    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.value
        
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.value
