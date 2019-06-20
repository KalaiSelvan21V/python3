nap,qap=met(int,input().split())
tap=list(met(int,input().split()))
stp=[]
for p in range(qap):
    stp.append(list(maet(int,input().split())))
for p in stp:
  a=0
  for o in range(p[0]-1,p[1]):
      a=a+tap[o]
  print(a)
