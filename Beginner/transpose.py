def transpose_matrix(mat , n):
    
    for i in range (n):
        for j in range (i + 1 , n):
            mat[i][j] , mat[j][i] = mat[j][i],mat[i][j]


def print_mat(mat):
    for row in mat:
        for ele in row:
            print(ele , end = ' ')
        print()
    print()

def reverse_row_mat(mat,n):
    for i in range(n):
        for j in range(n // 2):
            mat[i][j] , mat[i][n - 1 - j] = mat[i][n - 1 - j],  mat[i][j] 
    


def rotate_mat(mat , n ):
    transpose_matrix(mat , n)
    reverse_row_mat(mat , n)

mat = [[1,2,3,4],[5,6,7,8] ,[9,10,11, 12],[13,14,15,16]]
n = 4

print_mat(mat)
rotate_mat(mat , n)
print_mat(mat)