column=7
row=4
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i in [0,1,2,4,5,6]:
            if j==0 or j==3:
                print(a, end=' ')
            else:
                print(s, end=' ')
        else:
            print(a,end=" ")
    print()