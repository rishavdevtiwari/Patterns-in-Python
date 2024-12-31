column=7
row=7
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==3:
            if j==3:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==1 or i==5:
            if j==1 or j==5:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==2 or i==4:
            if j==2 or j==4:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            if j==0 or j==6:
                print(a,end=" ")
            else:
                print(s,end=" ")
    print()