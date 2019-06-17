g=int(input())
k=[int(i) for i in input().split()]
l=0
for i in range(g):
    for u in range(i):
        if k[u]<k[i]:
            l+=s[u]
print(l)
