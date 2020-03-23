def reorder_students(L):
    '''
    Input:  L    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    n = int(L.size/2)
    middle = L.head
    for i in range(n-1):
        middle = middle.next
    current = middle.next
    nxt = None
    while current is not None:
        temp = current.next #get the value that originally came after current. In the case of the original last item, it will be None
        current.next = nxt #this is where we turn the pointer around and make it point to teh previous one
        nxt = current #the node we are currently on is going to be the next one in the new sequence, so we call it next
        current = temp #now we move on to the one that came after current originally
    middle.next = nxt
    return L
