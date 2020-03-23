def ship_server_stats(R, s, t):
    '''
    Input:  R | a list of route tuples
            s | string name of origin city
            t | string name of destination city
    Output: w | maximum weight shippable from s to t
            c | minimum cost to ship weight w from s to t
    '''
    w, c = 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    #create relevant dictionaries
    succ = dict()
    wt_capacities = dict()
    costs = dict()
    for start_city, end_city, wt_capacity, cost in R:
        if start_city not in succ:
            succ[start_city] = set([end_city])
        else:
            succ[start_city].add(end_city)
        if start_city not in wt_capacities:
            wt_capacities[start_city] = dict()
            wt_capacities[start_city][end_city] = wt_capacity    
        else:
            wt_capacities[start_city][end_city] = wt_capacity  
        if start_city not in costs:
            costs[start_city] = dict()
            costs[start_city][end_city] = cost    
        else:
            costs[start_city][end_city] = cost 
        if end_city not in succ:
            succ[end_city] = set()
    #now lets run a dijkstras to find w
    w = dijkstra_wts(succ, wt_capacities, s, t)
    #now lets run another dijkstras to find c
    c = dijkstra(succ, s, t, wt_capacities, costs, w)
    return w, c


def dijkstra_wts(succ, wt_capacities, source_name, target_name):
        width = dict()
        for city in succ:
            width[city] = float('-inf')
        
        width[source_name] = float('inf')
        Q = set(city for city in succ)
        while Q:
            u = max(Q, key= lambda key: width[key])
            Q.discard(u)
            if width[u] == float('-inf'):
                break
            
            for v in succ[u]:
                alt = max(width[v],min(width[u], wt_capacities[u][v]))
                if alt > width[v]:
                    width[v] = alt
        
        return width[target_name]
    

def dijkstra(Adj, source_node, target_node, widths,costs,max_width):
    length = dict()
    for city in Adj:
        length[city] = float('inf')
    
    length[source_node] = 0
    Q = set(city for city in Adj)
    while Q:
        u = min(Q, key= lambda key: length[key])
        Q.discard(u)
        if length[u] == float('inf'):
            break
        
        for v in Adj[u]:
            if length[v] > length[u] + costs[u][v] and widths[u][v] >= max_width:
                length[v] = length[u] + costs[u][v]
    
    return length[target_node]

