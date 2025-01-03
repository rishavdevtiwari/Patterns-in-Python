column=7
row=5
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i in [0,3,4,5]:
            if j==2:
                print(a,end=" ")
            else:
                print(s,end=" ")
        elif i==1:
            if j==1 or j==2:
                print(a,end=" ")
            else:
                print(s,end=" ")
        elif i==2:
            if j==0 or j==2:
                print(a,end=" ")
            else:
                print(s,end=" ")
        else:
            print(a,end=" ")
    print()
        