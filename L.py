column=6
row=4
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==0 or i==1 or i==2 or i==3 or i==4:
            if j==0:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            print(a,end=" ")
    print()