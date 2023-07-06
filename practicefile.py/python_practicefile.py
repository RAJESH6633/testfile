n=5
for i in range(0,n+1):
    for j in range(n+1):
        print('*',end=' ')
    print()
print(f'i am printing the stars')


n=5
st=1
sp=0
for i in range(0,n):
    for j in range(0,sp):
        print(' ',end=' ')
    for k in range(0,st):
        print('*',end=' ')
    print()
    st+=1

n=5
sp=0
st=n
for i in range(0,n):
    for j in range(0,sp):
        print(' ',end=' ')
    for k in range(0,st):
        print('*',end=' ')
    print()
    sp-=0
    st+=1


n=6
for i in range(0,n):
    for j in range(0,n):
        if i==1 or i==2:
            print('@',end=' ')
        elif i==3:
            print('#',end=' ')
        elif i>3:
            print('*',end=' ')
    print()


n=5
for i in range(0,n):
    for j in range(0,n):
        if i%2==0:
            print('$',end=' ')
        else:
            print('*',end=' ')
    print()

n=5
count=0
for i in range(0,n):
    for j in range(0,n):
        print(chr(65+count),end=' ')
        count+=1
    print()

n=5
for i in range(0,n):
    for j in range(0,n):
        print(chr(65+j),end=' ')
    print()

