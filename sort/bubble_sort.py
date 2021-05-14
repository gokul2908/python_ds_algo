#bubble_sort

b = [1,3,2,4,7,3,4,2,22,34,3,23,44,22,11,33,22,5,32,34,1]

def bub(a):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            else:
                pass
        print(f'j current value is {j}', a)
    return a

print(bub(b))
print(b)

