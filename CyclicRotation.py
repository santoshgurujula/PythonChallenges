def solution(A,K):
    #print(A)
    array_len=len(A)
    if array_len ==0:
        return A
    iterations=K%array_len
    #print(iterations)
    for i in range(iterations):
        last_ndex_value=A[array_len-1]
        next_index_value=A[0]
        for j in range(array_len-1):
            A[j+1],next_index_value=next_index_value,A[j+1]
        A[0]=last_ndex_value
    return A

A=[]
K=8
print(solution(A,K))