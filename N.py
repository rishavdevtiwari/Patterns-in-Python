column=6
row=6
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==1:
            if j==0 or j==1 or j==5:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==2:
            if j==0 or j==2 or j==5:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==3:
            if j==0 or j==3 or j==5:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==4:
            if j==0 or j==4 or j==5:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            if j==0 or j==5:
                print(a,end=" ")
            else:
                print(s,end=" ")
    print()