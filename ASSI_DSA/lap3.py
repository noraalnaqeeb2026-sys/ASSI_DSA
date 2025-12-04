# LinkedList Class 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_n = Node(data)
        new_n.next = self.head
        self.head = new_n

    def insert_at_tail(self, data):
        new_n = Node(data)
        if not self.head:
            self.head = new_n
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_n

    def search(self, key):
        p = self.head
        while p:
            if p.data == key:
                return True
            p = p.next
        return False

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return

        prev = None
        cur = self.head
        while cur:
            if cur.data == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def print_list(self):
        q = self.head
        while q:
            print(q.data, end=" -> ")
            q = q.next
        print("None")

    def count_nodes(self):
        total = 0
        p = self.head
        while p:
            total += 1
            p = p.next
        return total


# Run
l = LinkedList()
l.insert_at_head(5)
l.insert_at_tail(15)
l.insert_at_tail(25)
l.print_list()
print("Search 15:", l.search(15))
l.delete(15)
l.print_list()
print("Nodes:", l.count_nodes())
