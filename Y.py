column=5
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0:
            if j==0 or j==4:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==1:
            if j==1 or j==3:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            if j==2:
                print(a,end=" ")
            else:
                print(s,end=" ")
    print()