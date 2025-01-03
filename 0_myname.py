column=7 #fixed
row=37
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i==1 or i==2:
            if j in [0,4,8,12,17,21,23,27,29,35]:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i==4:
            if j in [0,2,8,15,17,21,23,27,30,34]:
                print(a, end=' ')
            else:
                print(s,end=' ')
        elif i==5:
            if j in [0,3,8,15,17,21,23,27,31,33]:
                print(a, end=' ')
            else:
                print(s,end=' ')
        elif i==6:
            if j in[0,4,6,7,8,9,10,12,13,14,17,21,23,27,32]:
                print(a, end=' ')
            else:
                print(s,end=' ')
        elif i==3:
            if j in [0,1,2,3,8,13,14,17,18,19,20,21,23,24,25,26,27,29,35]:
                print(a, end=' ')
            else:
                print(s,end=' ')
        elif i==0:
            if j in [4,5,11,12,15,16,18,19,20,22,23,27,28,30,31,32,33,34,36]:
                print(s, end=' ')
            else:
                print(a,end=' ')
    print()