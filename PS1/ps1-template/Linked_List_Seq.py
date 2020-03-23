class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i == 0:  return self
        assert self.next
        return self.next.later_node(i - 1)

class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):  
        return self.size

    def __str__(self):  
        return '(' + ')->('.join([str(x) for x in self]) + ')'

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, A):
        for a in reversed(A):
            self.insert_first(a)

    def get_at(self, i):
        assert 0 <= i < len(self)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        assert 0 <= i < len(self)
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):         
        assert len(self) > 0
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        assert 0 <= i <= len(self)
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        assert 0 <= i < len(self)
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):   
        self.insert_at(len(self), x)

    def delete_last(self):      
        return self.delete_at(len(self) - 1)
