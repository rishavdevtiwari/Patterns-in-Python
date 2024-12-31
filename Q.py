column=6
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==1 or i==2:
            if j==0 or j==4:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==0 or i==4:
            if j==0 or j==4:
                print(s, end=' ')
            else:
                print(a,end=' ')
        elif i==3:
            if j==1 or j==3:
                print(s,end=' ')
            else:
                print(a,end=' ')
        else:
            if j==4:
                print(a,end=" ")
            else:
                print(s,end=" ")
    print()