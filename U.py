column=5
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0 or i==1 or i==2 or i==3:
            if j==0 or j==4:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            if j==0 or j==4:
                print(s,end=" ")
            else:
                print(a,end=" ")
    print()