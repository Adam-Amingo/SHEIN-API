def two_sum(arr , n , target):
    for i in range(n):
        for j in range(i + 1 , n):
            if(arr[i] + arr[j] == target):
                return [i , j]
        return[-1 , -1]
    

arr = [2 , 11 , 15 , 7]
target = 9
n = len(arr)
res= two_sum(arr , n , target)
print(res)


#######################
####################
##contains duplcate#################

def contains_duplicate(arr , n):
    for i in range(n):
        for j in range(i+ 1 , n):
            if (arr[i] == arr[j]):
                return True
    return False
            
arr = [2 , 11 , 15 , 7]
n =len(arr)
res1 = contains_duplicate(arr, n)
print(res1)
