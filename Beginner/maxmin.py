# def find_max(arr):
#     max = arr[0]
#     n = len(arr)
#     for i in range (1 , n):
#         if(arr[i] > max):
#             max = arr[i]
#     return max

# def find_min(arr):
#     min = arr[0]
#     n = len(arr)

#     for i in range (1 , n):
#         if (min > arr[i]):
#             min = arr[i]
#     return min


# arr = [45 ,22 , -3 , 56 , 12, 73 , -15 , -34 ]
# min_val = find_min(arr)
# max_val = find_max(arr)
# print(max_val)
# print(min_val )


#########################################
######################################

def find_kth_max(arr , n , k):
    for j in range(k):
        max = j
        for i in range(j + 1 , n):
            if(arr[i] > arr[max] ):
                max = i 
        arr[j] , arr[max] = arr[max] , arr[j]

    return arr[ k - 1]


arr = [45 ,22 , -3 , 56 , 12, 73 , -15 , -34 ]
n = len(arr)
k = 2
res = find_kth_max(arr , n , k)
print(res)


#########################
########################

def find_kth_min(arr , n , k):
    for i in range (k):
        min = i 
        for j in range(i + 1 , n):
            if (arr[min] > arr[j]):
                min = j 
        arr[i] , arr[min] = arr[min] , arr[i]
    return arr[k -1 ]


arr = [45 ,22 , -3 , 56 , 12, 73 , -15 , -34 ]
n = len(arr)
k = 8
res = find_kth_min(arr , n , k)
print(res)
