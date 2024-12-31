column=6
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0:
            if j==0 or j==4:
                print(s, end=' ')
            else:
                print(a, end=' ')
        elif i==1 or i==2 or i==4 or i==5:
            if j==0 or j==4:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            print(a,end=" ")
    print()