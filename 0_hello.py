column=7
row=25
a="*"
s=" "
for i in range(0,column):
    for j in range(0,row):
        if i in [1,2,4,5]:
            if j in [0,4,6,11,16,21,24]:
                print(a, end=' ')
            else:
                print(s, end=' ')
        elif i in [3]:
            if j in [5,10,12,13,14,15,17,18,19,20,22,23]:
                print(s,end=' ')
            else:
                print(a,end=' ') 
        elif i in [6]:
            if j in [1,2,3,5,10,15,20]:
                print(s,end=' ')
            else:
                print(a,end=' ')
        else:
            if j in [1,2,3,5,10,12,13,14,15,17,18,19,20]:
                print(s,end=' ')
            else:
                print(a,end=' ')
    print()