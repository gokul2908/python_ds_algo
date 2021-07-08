def twoSum(nums, target: int):
    dict = {}
    for index, element in enumerate(nums):
        if element in dict:
            dict[element].append(index)
        else:
            dict[element] = [index]

    for element in dict:
        find = (target-element)
        if find in dict and element != find:
            return [dict[element][0], dict[find][0]]
        if find == element and len(dict[element]) == 2:
            return dict[element]
