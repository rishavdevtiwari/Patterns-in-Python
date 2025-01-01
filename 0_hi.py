column=7
row=13
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i in [1,2,4,5]:
            if j==0 or j==4 or j==9:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i in [3]:
            if j==5 or j==6 or j==7 or j==8 or j==10 or j==11 or j==12:
                print(s,end=' ')
            else:
                print(a,end=' ')   
        else:
            if j==1 or j==2 or j==3 or j==5:
                print(s,end=' ')
            else:
                print(a,end=' ')
    print()