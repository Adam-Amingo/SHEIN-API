def find_element(arr , target):
    for ele in arr:
        if(ele == target):
            return True
    return False

 


arr = [4 , 5, 67, 89, 19]
target = 89
res = find_element(arr , target)
print(res)