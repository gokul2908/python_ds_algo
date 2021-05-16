# To determine binary possibilities from number of bits
from guppy import hpy

h = hpy()
'''for n is 3 
A = [000 100 010 110 001 101 011 111]
'''
import time
start = time.time()

n =  15 #number of bits

def binary(n):
    A = ["0", "1"]
    while n > 1:
        n -= 1
        A = A + A
        for i in range(len(A)):
            if i < len(A)/2:
                A[i] = "0"+A[i]
            else:
                A[i] ="1"+ A[i]
    return print(A)

(binary(n))

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")
print(h.heap())