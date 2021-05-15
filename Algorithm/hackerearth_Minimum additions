T = input()     #No. of test case

def average_of_aray(A):
    sumofarray = 0
    for j in range(len(A)):
        sumofarray = (sumofarray + A[j])
    return int(sumofarray / len(A))

for i in range(int(T)):
    N_K = [int(x) for x in input().split()]
    N = N_K[0]
    K = N_K[1]
    A = [int(x) for x in input().split()]
    
    avg = average_of_aray(A) 
    number_int_to_add = 0

    while avg > K:
        number_int_to_add += 1
        A.append(0)
        avg = average_of_aray(A)
    print(number_int_to_add)