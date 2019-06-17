k=int(input())
a=list(map(int,input().split()))
s=0
for c in range(len(a)-2):
   for y in range(i+1,len(a)-1):
         for v in range(y+1,len(a)):
            if a[c]<a[y]<a[j] and c<x<v:
                s+=1
print(s)   
