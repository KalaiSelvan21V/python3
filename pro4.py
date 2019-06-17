string3,string4=input().split()
f=0
if len(string3)>len(string4):
  string3,string4=string4,string3
h=0
while h<len(string3):
  f+=(ord(string4[j])-ord(string3[h]))
  h+=1
for h in range(h,len(string4)):
  f+=ord(string4[h])-ord('b')+1
print(f)
