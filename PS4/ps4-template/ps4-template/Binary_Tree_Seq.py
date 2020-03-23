from Binary_Tree    import Binary_Node, Binary_Tree

class Size_Node(Binary_Node):
    def subtree_update(A):                  # O(1)
        super().subtree_update()
        A.size = 1
        if A.left:   A.size += A.left.size
        if A.right:  A.size += A.right.size

    def subtree_node_at(A, i):              # O(h)
        assert 0 <= i < A.size
        if A.left:        L_size = A.left.size
        else:             L_size = 0
        if i < L_size:    return A.left.subtree_node_at(i)
        elif i > L_size:  return A.right.subtree_node_at(i - L_size - 1)
        else:             return A

class Binary_Tree_Seq(Binary_Tree):
    def __init__(self): super().__init__(Size_Node)

    def build(self, A):                     # O(n)
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:   
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root
        self.root = build_subtree(A, 0, len(A) - 1)
        self.size = self.root.size
        
    def get_at(self, i):                    # O(h)
        assert self.root
        return self.root.subtree_node_at(i).item

    def set_at(self, i, x):                 # O(h)
        assert self.root
        self.root.subtree_node_at(i).item = x

    def insert_at(self, i, x):              # O(h)
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:    
                self.root = new_node
        else:
            node = self.root.subtree_node_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1

    def delete_at(self, i):                 # O(h)
        assert self.root
        node = self.root.subtree_node_at(i)
        ext = node.subtree_extract()
        if ext.parent is None:  self.root = None
        self.size -= 1
        return ext.item

    def insert_first(self, x):  self.insert_at(0, x)
    def delete_first(self):     return self.delete_at(0)
    def insert_last(self, x):   self.insert_at(len(self), x)
    def delete_last(self):      return self.delete_at(len(self) - 1)
