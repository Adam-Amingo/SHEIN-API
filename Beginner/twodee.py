############################
############################

arr = [ [1,2,3],[4,5,6],[7,8,9]]

for i in range(len(arr)):
    for j in range(0, len(arr[i])):
        print(arr[i][j] , end =' ')
    
    print()

#########################
#####################

for row in arr:
    for col in row:
        print(col , end = ' ')
    print()


    ############################
    ##################FIND DIAGONAL SUM#########

def find_diagonal_sum(arr, n):
        pd_sum = 0
        sd_sum =0

        for i in range(n):
            for j in range(n):

                if (i == j ):
                    pd_sum += arr[i][j]
                
                if( i == n -1 - j):
                    sd_sum += arr[i][j]
        
        print('Principal diagonal sum =' ,pd_sum)
        print('secondary diagonal sum =' ,sd_sum)


arr = [ [1,2,3],[2,4,6],[5,6,7]]
n= 3
# find_diagonal_sum(arr , n)

######################
#####################
##############considering big o #################

def find_diagonaal_sum(arr , n):
    pd_sum = 0 
    sd_sum = 0
    for i in range(n):
        pd_sum += arr[i][i]
        sd_sum += arr[i][n - 1 - i]
    
    print('Principal diagonal sum =' ,pd_sum)
    print('secondary diagonal sum =' ,sd_sum)


arr = [ [1,2,3],[4,5,6],[7,8,9]]
n= 3
find_diagonaal_sum(arr , n)