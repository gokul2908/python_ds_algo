#insertion_sort.py

b = [3,1,3,2,4,7,3,4,2,22,34,3,23,44,22,11,33,22,5,32,34,1,1]

def ins(a):
    c =[]
    c.append(a[0])
    for i in range(1,len(a)):
        k = 0
        c.append(a[i])
        while i!=k:
            if c[i]>=c[k]:
                pass
            else:
                c.insert(k,c[i])
                c.pop(i+1)
                break
            k = k+1
    return c

print(ins(b))
