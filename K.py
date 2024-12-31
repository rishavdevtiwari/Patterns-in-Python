column=6
row=4
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0 or i==6:
            if j==1 or j==2:
                print(s, end=' ')
            else:
                print(a, end=' ')
        elif i==1 or i==5:
            if j==1 or j==3:
                print(s, end=' ')
            else:
                print(a, end=' ')
        elif i==2 or i==4:
            if j==2 or j==3:
                print(s, end=' ')
            else:
                print(a, end=' ')
        else:
            if j==0:
                print(a,end=" ")
            else:
                print(s,end=' ')
    print()