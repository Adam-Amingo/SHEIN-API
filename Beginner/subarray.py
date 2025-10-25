def generate_subarrays(arr):
    n = len(arr)

    for i in range (0 , n-1):
        for j in range (i , n): 
            print( arr[i: j + 1])


arr = [1 ,2 ,3 ]
generate_subarrays(arr)