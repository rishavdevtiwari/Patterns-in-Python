column=5
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==1:
            if j==3:
                print(a,end=" ")
            else:
                print(s,end=" ")
        elif i==2:
            if j==2:
                print(a,end=" ")
            else:
                print(s,end=" ")
        elif i==3:
            if j==1:
                print(a,end=" ")
            else:
                print(s,end=" ")
        else:
            print(a,end=" ")
    print()