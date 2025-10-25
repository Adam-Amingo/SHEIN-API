def substring(str, n):
    for i in range (0 , n- 1):
        for j in range( i, n + 1):
            print(str[i : j ])
        

def reverse_string(str):
    return str[::-1]
        
        




str = 'abcdef'
n = len(str)
# substring(str, n)
res = reverse_string(str)
print(res)


