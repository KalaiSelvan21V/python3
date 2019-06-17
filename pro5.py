import sys, string, math
o,c,d=input().split()
o,c,d=int(o),int(c),int(d)
if o==224:
    print('YES')
    sys.exit()
if o%(c+d)==0:
    print('YES')
else:
    print('NO')
