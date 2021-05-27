def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        L = arr[:mid]
        R = arr[mid:]
        L = merge_sort(L)
        R = merge_sort(R)
        arr = merge_array(L,R)
        return arr
    else: return arr

def merge_array(left,right):
    j = 0
    for i in right:
        while True:
            try:
                if i < left[j]:
                    left.insert(j,i)
                    break
            except:
                left.append(i)
                break
            j += 1
    return left

arr = [1,4,2,6,3,6,8,4,12,4,7,11,22,112,543,43,642,-21]
print(len(arr))
print(merge_sort(arr))

