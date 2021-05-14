limit = 5
values = [1,1,1,1, 1, 2, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3]


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

values = ins(values)


freq = []
k = 0
for i in range(len(values)):
    if k !=0:
        k = k-1
        pass
    else: 
        j = i
        counter = 0
        k = -1
        while values[i] == values[j]:
            counter = counter + 1
            k = k + 1
            j = j + 1
            if j == len(values): break
        freq.append(counter)



maximum = freq.index(max(freq))
x = 0
for i in range(maximum):
    x = freq[i]+x

print(values[x])