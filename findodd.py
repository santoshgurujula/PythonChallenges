# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    k = int()
    A.sort()
    if(len(A)) == 0:
        return None
    elif(len(A)) == 1:
        return A[0]
    else:
        for i in range(len(A)):
            try:
                if (A[i] == A[i+1]):
                    # print('OK',A[i],A[i+1],sep='-')
                    continue
                else:
                    # print('NOT OK',A[i],A[i+1],sep='-')
                    try:
                        if(A[i] == A[i-1]):
                            # print('OK',A[i],A[i-1],sep='=')
                            continue
                        else:
                            k = A[i]
                            # print('NOT OK',A[i])
                            break
                    except IndexError:
                        k = A[i]
                        # print('Culprit is ',A[i])
                        break
            except  IndexError:
                if(A[i]==A[i-1]):
                    k=None
                else:
                    k=A[i]
                    # print('Culprit is ',A[i])
                    break           
    return k
