import numpy as np
def equation(A):
    values = []
    for i in range(len(A)): # to get variable values
        if A[i] == "=" or A[i] == "*" or A[i] == "/":
            pass
        else:
            values.append(input(A[i]+" : "))
            if values[len(values)-1] == "":
                unknown = A[i]

    ''' A = [ 'x', '=', 'y', '/', 'z']
        values = ['', 4, 3]
    '''
    # Rearranging equation
    X = [] #product
    Y = [] #divide
    
    if A.index(unknown) < A.index("="): # x unknown
        for i in range(1,len(values)):
            if i < (A.index("/")-1):
                X.append(int(values[i]))
            else:
                Y.append(int(values[i]))
    elif A.index(unknown) < A.index("/"): # y unknown
        X.append(int(values[0]))
        for i in range(1,len(values)):
            if i < (A.index("/")-1):
                if values[i] == "":
                    pass
                else:
                    Y.append(int(values[i]))
            else:
                X.append(int(values[i]))
    else: # z unknown
        Y.append(int(values[0]))
        for i in range(1,len(values)):
            if i < (A.index("/")-1):
                X.append(int(values[i]))
            else:
                if values[i] == "":
                    pass
                else:
                    y.append(int(values[i]))

    return np.product(X)/np.product(Y)
    
eqn = "X = Y a r1 / Z r b"
A = eqn.split()
print("your answer is "+ str(equation(A)))