def count_paths(F):
    '''
    Input:  F | size-n direct access array of size-n direct access arrays
              | each F[i][j] is either 't', 'm', or 'x'
              | for tree, mushroom, empty respectively
    Output: m | the number of distinct optimal paths in F
              | starting from (0,0) and ending at (n-1,n-1)
    '''
    p = 0
    ##################
    # YOUR CODE HERE #
    ##################
    memoX = dict()
    memoY = dict()
    
    def X(i,j):
        try:
            return memoX[i][j]
        except:
            pass
        if not (0<=i<len(F) and 0<=j<len(F)):
            ans = 0
            if i in memoX:
                memoX[i][j] = ans
            else:
                memoX[i] = dict()
                memoX[i][j] = ans
            return ans
        elif i==0 and j==0:
            ans = 0
            if i in memoX:
                memoX[i][j] = ans
            else:
                memoX[i] = dict()
                memoX[i][j] = ans
            return ans
        else:
            if F[i][j] == 't':
                ans = 0
                if i in memoX:
                    memoX[i][j] = ans
                else:
                    memoX[i] = dict()
                    memoX[i][j] = ans
                return ans
            elif F[i][j] == 'm':
                ans = max(X(i-1,j) + 1, X(i,j-1) + 1)
                if i in memoX:
                    memoX[i][j] = ans
                else:
                    memoX[i] = dict()
                    memoX[i][j] = ans
                return ans
            else:
                ans = max(X(i-1,j), X(i,j-1))
                if i in memoX:
                    memoX[i][j] = ans
                else:
                    memoX[i] = dict()
                    memoX[i][j] = ans
                return ans
            
    def Y(i,j):
        def m(i,j):
            if F[i][j] == 'm':
                return 1
            else:
                return 0
            
        try:
            return memoY[i][j]
        except:
            pass
        
        if not (0<=i<len(F) and 0<=j<len(F)):
            ans = 0
            if i in memoY:
                memoY[i][j] = ans
            else:
                memoY[i] = dict()
                memoY[i][j] = ans
            return ans
        elif i==0 and j==0:
            ans = 1
            if i in memoY:
                memoY[i][j] = ans
            else:
                memoY[i] = dict()
                memoY[i][j] = ans
            return ans
        else:
            cond1 = X(i-1,j) == X(i,j) - m(i,j)
            cond2 = X(i,j-1) == X(i,j) - m(i,j)
            if cond1 and cond2:
                ans = sum([Y(i-1,j), Y(i,j-1)])
                if i in memoY:
                    memoY[i][j] = ans
                else:
                    memoY[i] = dict()
                    memoY[i][j] = ans
                return ans
            elif cond1:
                ans = sum([Y(i-1,j)])
                if i in memoY:
                    memoY[i][j] = ans
                else:
                    memoY[i] = dict()
                    memoY[i][j] = ans
                return ans 
            elif cond2:
                ans = sum([Y(i,j-1)])
                if i in memoY:
                    memoY[i][j] = ans
                else:
                    memoY[i] = dict()
                    memoY[i][j] = ans
                return ans 
            else:
                ans = 0
                if i in memoY:
                    memoY[i][j] = ans
                else:
                    memoY[i] = dict()
                    memoY[i][j] = ans
        
    p = Y(len(F)-1,len(F)-1)
    return p
