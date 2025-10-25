def spiral_traverse(mat , n ,m):
    left = 0 
    right = n - 1
    top = 0 
    bottom = m - 1
    count = 0
    res =[]

    while(count < m * n):
        if (count >= m*n):
            break
        for j in range (left , right + 1 ):
            i = top
            res.append(mat[i][j])
            # print(mat[i][j], end = ' ')
            count += 1

        if (count >= m*n):
            break
        for i in range(top + 1 ,bottom  + 1 ):
            j = right
            # print(mat[i][j] , end = ' ')
            res.append(mat[i][j])
            count += 1

        if (count >= m*n):
            break
        for j in range(right - 1 , left -1, -1):
            i = bottom 
            # print(mat[i][j] , end = ' ')
            res.append(mat[i][j])
            count += 1

        if (count >= m*n):
            break
        for i in range(bottom -1 , top ,- 1):
            j = left
            # print(mat[i][j] , end = ' ')
            res.append(mat[i][j])
            count += 1
        
        left+= 1
        right -= 1
        top += 1
        bottom -= 1

    return res


def print_ele(mat):
    for row in mat:
        for ele in row:
            print(ele , end= ' ')
        print()
    print()
    



mat = [[1,2,3,4,17] , [5,6,7,8,18] ,[9,10,11,12,19],[13,14,15,16,20],[21,22,23,24,25]]
n = 5
m= 5

print_ele(mat)
answer = spiral_traverse(mat, n , m)
print(answer)
