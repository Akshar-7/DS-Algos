def pw(x,y,m):
    res=1; x%=m
    while(y>0):
        if(y&1): res=res*x %m
        x=x*x %m
        y>>=1
    return res

def cmpst(n, a, d, s):
    x = pw(a,d,n)
    if (x==1 or x==n-1): return False
    for r in range(1,s):
        x = x*x %n
        if (x==n-1): return False
    return True

def M_R(n):
    if (n<2): return False
    r = 0
    d = n-1
    while ((d&1)==0):
        d>>=1; r+=1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if (n==a): return True
        if (cmpst(n, a, d, r)): return False
    return True
