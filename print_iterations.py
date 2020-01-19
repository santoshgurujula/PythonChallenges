itr=int(input())
for i in range(1,itr+1):
    for k in range(itr-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
for i in range(itr-1,0,-1):
    for k in range(itr-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()