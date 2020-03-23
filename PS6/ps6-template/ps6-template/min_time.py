import copy
def min_time(C, D):
    '''
    Input:  C | a list of code pairs
            D | a list of dependency pairs
    Output: t | the minimum time to complete the job, 
                or None if the job cannot be completed
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    
    #D = set(D)
    #C = set(C)
    starter_vertices = set([x[0] for x in C]) #these iwll be the nodes we connect our supernode to
    wt_dict = {k:-v for (k,v) in C}
    adj_dict = {k:set() for k in starter_vertices} #maps filenames -> children filenames
    reverse_adj_dict = {k:set() for k in starter_vertices} #maps filenames -> parent filenames
    for source_filename,destination_filename in D:
        adj_dict[source_filename].add(destination_filename)
        starter_vertices.discard(destination_filename)
        reverse_adj_dict[destination_filename].add(source_filename)
        
    def w(u,v): #define our weight method
        if v in adj_dict[u]:
            return wt_dict[u]
        else:
            raise TypeError 
    
    adj_dict['supernode'] = starter_vertices
    wt_dict['supernode'] = 0
    d, parent = DAG_Shortest_Paths(adj_dict, w, 'supernode', reverse_adj_dict)
    if not d:
        return None
    ret_dict = dict()
    m = min(d.values())
    for k,v in d.items():
        if v == m:
            ret_dict[k] = v + wt_dict[k]
    return abs(min(ret_dict.values()))

def relax(Adj, w, d, parent, u, v):
    if d[v] > d[u] + w(u, v): # better path through vertex u
        d[v] = d[u] + w(u, v) # relax edge with shorter path found
        parent[v] = u
        
def DAG_Shortest_Paths(Adj, w, s, reverse_Adj): # Adj: adjacency list, w: weights, s: start
    order = dfs_alt(Adj, reverse_Adj, s) # run depth-first search on graph
    if not order:
        return False, False
    d = {_:float('inf') for _ in Adj} # shortest path estimates d(s, v)
    parent = {_:None for _ in Adj} # initialize parent pointers
    d[s], parent[s] = 0, s # initialize source
    for u in order: # loop through vertices in topo sort
        for v in Adj[u]: # loop through out-going edges of u
            relax(Adj, w, d, parent, u, v) # relax edge from u to v
    return d, parent # return weights, paths via parents

def dfs_alt(Adj, reverse_Adj, s):
    """
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edges
    while S is non-empty do
        remove a node n from S
        add n to tail of L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S
    if graph has edges then
        return error (graph has at least one cycle)
    else 
        return L (a topologically sorted order)
    """
    Adj = copy.deepcopy(Adj)
    L = []
    S = [s]
    while S:
        n = S.pop()
        L.append(n)
        nbs = Adj[n].copy()
        for neighbor in nbs:
            Adj[n].discard(neighbor)
            reverse_Adj[neighbor].discard(n)
            if not reverse_Adj[neighbor]:
                S.append(neighbor)
    if any(Adj.values()):
        return None
    else:
        return L
            
    