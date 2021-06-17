matrix = [
    [1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1]
]

border_con = {}

def key_gen(row, col):
    return f'{row}{col}'

def border_land(matrix):
    max_row = len(matrix)-1
    max_col = len(matrix[0])-1
    for row,j in [(0,matrix[0]), (max_row,matrix[-1])]:
        for col,i in enumerate(j):
            if i == 1: 
                key = key_gen(row,col)
                border_con[key] = True
    
    for index,j in enumerate(matrix[1:max_row],1):
        if j[0] == 1: 
            key = key_gen(index,0)
            border_con[key] = True
        if j[-1] == 1: 
            key = key_gen(index,max_col)
            border_con[key] = True

def rec(matrix, row, col, prev="-1-1"):
    near_by = (
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 0)
    )
    for i, j in near_by:
        key = key_gen(row+i, col+j)
        if key in border_con:
            border_con[key_gen(row, col)] = True
            break
        elif matrix[row+i][col+j] == 1 and prev != key:
            rec(matrix, row+i, col+j, key_gen(row, col))

def inner(matrix):
    for index_r, row in enumerate(matrix[1:len(matrix)-1], 1):
        for index_c, col in enumerate(row[1:len(row)-1], 1):
            if matrix[index_r][index_c] == 1:
                rec(matrix, index_r, index_c)

border_land(matrix)
inner(matrix)

for index_r, row in enumerate(matrix[1:len(matrix)-1], 1):
    for index_c, col in enumerate(row[1:len(row)-1], 1):
        if matrix[index_r][index_c] == 1 and key_gen(index_r, index_c) not in border_con:
            matrix[index_r][index_c] = 0

for i in matrix:
    print(i)
