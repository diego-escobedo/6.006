def get_damages(H):
    '''
    Input:  H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]
    H_alt = [(x,i) for i,x in enumerate(H)]
    arr, dmg_array = mergesort_modified(H_alt, D)
    return dmg_array

def mergesort_modified(lst, dmg_array): 
    if len(lst) < 2:
        return lst
  
    middle = len(lst)//2
    
    l = mergesort_modified(lst[:middle], dmg_array)     
    try:
        left, dmg_array = l
    except ValueError:
        left = l
        
    r = mergesort_modified(lst[middle:], dmg_array) 
    try:
        right, dmg_array = r
    except ValueError:
        right = r
    
    return merge(left, right, dmg_array)

def merge(left, right, dmg_array): 
    if not len(left) or not len(right): 
        return left or right 
    
    arr = left+right
    
    special_index = None
    for i in range(len(arr) -1):
        if arr[i][0] > arr[i+1][0]: #if the number of bricks in i is greater than the number of bricks in i+1:
            special_index = i
            break
    if special_index is not None:
        lft = 0
        rgt = special_index + 1
        acc = 0
        while lft < special_index + 1:
            dmg_array[arr[lft][1]] += acc
            while rgt < len(arr) and arr[lft][0] > arr[rgt][0]:
                dmg_array[arr[lft][1]] += 1
                rgt += 1
                acc += 1
            lft += 1    
    
    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 
    return result, dmg_array

#H = [6, 7, 9, 0, 10]
#H_alt = [(x,i) for i,x in enumerate(H)]
#print(b_procedure(H_alt, [1,1,1,1,1]))