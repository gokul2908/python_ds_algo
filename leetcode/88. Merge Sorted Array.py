def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index = 0
    for idx, i in enumerate(nums2):
        while i>nums1[index] and index<=(m+idx-1):
            index += 1 
        idx2 = index
        while idx2<=(idx+m):
            i, nums1[idx2] = nums1[idx2], i
            idx2 += 1
        index += 1
        
merge([1,2,3,0,0,0],3,[2,5,6],3)