column=4
row=9
a='*'
s=' '
for i in range(0,row):
    for j in range(0,column):
        if i in [1,2,3,5,6,7]:
            if j==3:
                print(a,end=' ')
            else:
                print(s,end=' ')
        else:
            print(a,end=' ')
    print()