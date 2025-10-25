
def reverse_arr(arr , start ,end):
   diff = end - start
   for i in range(diff // 2 + 1):
      arr[start + i] , arr[end - i] = arr[end - i ] , arr[start + i]


def rotate_arr(arr , n , d):
   d = d % n 
   reverse_arr(arr , 0 , d - 1)
   reverse_arr(arr ,d , n - 1)
   reverse_arr(arr , 0 , n - 1)


arr = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ]

d = 3
n = len(arr)
rotate_arr(arr , n , d)
print(arr)


