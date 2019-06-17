from itertools import combinations
n1,n2=map(int,input().split())
a=len(str(n1))
b=list(combinations(str(n1),a-n2))
b=(sorted(b))
k="".join(b[0])
print(k)
