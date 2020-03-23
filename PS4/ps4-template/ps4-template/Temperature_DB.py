from Binary_Tree_Set import BST_Node, Binary_Tree_Set
# ----------------------------------- #
# DO NOT REMOVE THIS IMPORT STATEMENT # 
# DO NOT MODIFY IMPORTED CODE         #
# ----------------------------------- #


def _max(*args):    
    if all(x == None for x in args):
        return None
    else:
        return max(x for x in args if x is not None)

class Temperature_DB_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (A) HERE #
        # ------------------------------------ #
        if A.left and A.right: #right and left subtree
            A.max_temp = max(A.item.temp, A.left.max_temp, A.right.max_temp)
            A.min_date = A.left.min_date
            A.max_date = A.right.max_date
        elif A.right: #only right subtree
            A.max_temp = max(A.item.temp, A.right.max_temp)
            A.min_date = A.item.key
            A.max_date = A.right.max_date
        elif A.left: #only left subtree
            A.max_temp = max(A.item.temp, A.left.max_temp)
            A.min_date = A.left.min_date
            A.max_date = A.item.key
        else:
            A.max_temp = A.item.temp
            A.min_date = A.item.key
            A.max_date = A.item.key
    

    def subtree_max_in_range(A, d1, d2):
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (C) HERE #
        # ------------------------------------ #
        #case when A's subtree is completely contained within range
        if A.min_date >= d1 and A.max_date <= d2:
            return A.max_temp
            
        #case when A's subtree is completely out of range
        elif A.min_date > d2 or A.max_date < d1:
            return None
            
        #Case when partially overlapping, and A within range
        elif (A.item.key <= d2 and A.item.key >= d1):
            
            if A.left and A.right:
                return _max( A.item.temp, A.left.subtree_max_in_range(d1, d2), A.right.subtree_max_in_range(d1, d2) )
            elif A.right:
                return _max( A.item.temp, A.right.subtree_max_in_range(d1, d2) ) 
            elif A.left:
                return _max( A.item.temp, A.left.subtree_max_in_range(d1, d2) )
            else:
                return A.item.temp
            
        #Case when partially overlapping, and A not within range  
        else:
            if A.left and A.right:
                return _max( A.left.subtree_max_in_range(d1, d2), A.right.subtree_max_in_range(d1, d2) )
            elif A.right:
                return A.right.subtree_max_in_range(d1, d2)
            elif A.left:
                return A.left.subtree_max_in_range(d1, d2)
            else:
                return None


# ----------------------------------- #
# DO NOT MODIFY CODE BELOW HERE       # 
# ----------------------------------- #
class Measurement:
    def __init__(self, temp, date):
        self.key  = date
        self.temp = temp

    def __str__(self): 
        return "%s,%s" % (self.key, self.temp)

class Temperature_DB(Binary_Tree_Set):
    def __init__(self): 
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
