column=6
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==1:
            if j==2:
                print(s, end=' ')
            else:
                print(a, end=' ')
        elif i==2:
            if j==1 or j==3:
                print(s, end=' ')
            else:
                print(a, end=' ')
        else:
            if j==0 or j==4:
                print(a,end=" ")
            else:
                print(s,end=" ")
    print()