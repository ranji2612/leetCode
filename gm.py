def gm(A):
    next = [-1 for i in range(len(A))]
    s=[]
    for i in range(len(A)):
        x=A[i]
        k=x+1
        t=[]
        print s
        while len(s)>0:
            k,p = s.pop()
            print '--',k,p
            if k < x:
                print 'oooo'
                next[p] = x
            else:
                t.insert(0,(k,p))
        t.insert(0,(x,i))
        for e in t:
            s.append(e)
    return next