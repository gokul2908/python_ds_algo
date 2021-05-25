def insertion_sort(a): #insertion sort
    c =[]
    if len(a) > 0:
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
    return []


def quick_sort(arr):
    if len(arr) > 4:
        x = arr[int(len(arr)/2)]
        right = []
        left = []
        middle = []
        for i in range(len(arr)):
            if arr[i] > x:
                right.append(arr[i])
            elif arr[i] == x:
                middle.append(arr[i])
            else:
                left.append(arr[i])
        left = quick_sort(left)
        left.extend(middle)
        right = quick_sort(right)
        left.extend(right)
        return left
    else:
        return insertion_sort(arr)

arr = [1,4,2,6,3,6,8,4,12,4,7,11,22,112,543,43,642,-21]
print(quick_sort(arr))

