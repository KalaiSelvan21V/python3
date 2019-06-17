import math
import functools
c,d=map(int,input().split())
List=[int(k) for k in input().split()]
for k in range(d):
    aa,bb=map(int,input().split())
    s=functools.reduce(math.gcd,List[aa-1:bb])
    print(s)
