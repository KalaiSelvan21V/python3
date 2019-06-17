    
st3,st4=input().split()
b=abs(len(st3)-len(st4))
for i in range(len(st3)):
    if len(st4)==1 and st4[i] in st3:
        break
    if st3[i]!=st4[i]:
        b+=1
print(b)
