
def find_palindrom_permutation(str):

    #calculate frequency
    dict = {}
    for char in str :
        dict[char] = dict.get(char , 0) + 1
    
    #calculating the number of odd characters
    count= 0
    for key , val in dict.items():
        if val % 2 != 0 :
            count += 1 
    
    return count <= 1 






str = 'hello'
res = find_palindrom_permutation(str)
print(res)