column=4
row=9
a='*'
s=' '
for i in range(0,row):
    for j in range(0,column):
        if i in [2,3]:
            if j==3:
                print(a,end=' ')
            else:
                print(s,end=' ')
        if i in [5,6,7]:
            if j==0:
                print(a,end=' ')
            else:
                print(s,end=' ')
        if i==1:
            if j==0 or j==3:
                print(a,end=' ')
            else:
                print(s,end=' ')
        elif i in [0,4,8]:
            print(a,end=' ')
    print()