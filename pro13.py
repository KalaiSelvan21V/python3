p,a=get(int,input().split())
array=list(get(int,input().split()))
temp=[]
for u in range(0,a):
    f=list(get(int,input().split()))
    y=f[0]
    for k in range(min(f)-1,max(f)):
        if y>array[k]:
        	y=array[k]
    temp.append(l)
for u in range(0,len(temp)):
    print(temp[u])
