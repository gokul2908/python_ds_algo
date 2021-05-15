N = int(input())
A = [int(x) for x in input().split()]
print(len(set(A)))
A_2 = []
j = 0
A_2.append(A[0])
for i in range(1,N):
    
    if  A_2[j] == A[i]:
        pass
    else:
        A_2.append(A[i])
        j += 1

print(len(A_2))