def min_mod_tuple(A, k):
    pools = [[x for x in range(len(A))], [x for x in range(len(A))]]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool if y not in x]
    minim = 9999999999999999999
    ret = None
    for test in result:
        i,j = test
        if (A[i]*A[j])%k < minim:
            minim = (A[i]*A[j])%k
            ret = [i,j]
    return tuple(sorted(ret))