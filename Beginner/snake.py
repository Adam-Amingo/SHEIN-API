


def snake_pattern_printing(mat , n):
    res = []

    for i in range(0,n):
        if (i % 2 == 0):
            for j in range(0, n):
                res.append(mat[i][j])
        else:
            for j in range(n - 1 , -1 , -1):
                res.append(mat[i][j])
    
    print(res) 

def print_mat(mat ):
    for row in mat:
        for ele in row:
            print(ele , end = ' ')
        print() 
    print()



mat = [[1,2,3,4] , [5,6,7,8] ,[9,10,11,12],[13,14,15,16]]
n= 4
print_mat(mat )
snake_pattern_printing(mat , n)
