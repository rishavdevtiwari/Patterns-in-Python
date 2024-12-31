column=7
row=4
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0:
            if j==0:
                print(s, end=' ')
            else:
                print(a, end=' ')
        elif i==5:
            if j==0 or j==2:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==6:
            if j==3:
                print(s,end=' ')
            else:
                print(a,end=' ')
        else:
            if j==2:
                print(a,end=" ")
            else:
                print(s,end=' ')
    print()