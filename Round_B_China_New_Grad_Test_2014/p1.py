import sys
s=sys.stdin.readline
t=int(s())
for i in range(t):
    n=int(s())
    nn=n*n
    f=True
    m=[]
    r=[k+1 for k in range(nn)]
    for j in range(n*n):
        m.append(map(int,s().split()))
    mn=m 
    for j in range(nn):
        if not sorted(mn[j])==r:
            f=False
    mn=[[mm[k] for mm in m] for k in range(nn)]
    for j in range(nn):
        if not sorted(mn[j])==r:
            f=False
    mn=[[m[i1*n+i2][j1*n+j2] for i2 in range(n) for j2 in range(n)]for i1 in range(n) for j1 in range(n)]
    for j in range(nn):
        if not sorted(mn[j])==r:
            f=False
    if f:
        print "Case #%d: Yes"%(i+1)
    else:
        print "Case #%d: No"%(i+1)
