# s = {8,9,10,11,3,4}
# s1 = {1 ,2,3,4,5}

# new_set = s.union(s1)
# s3 = s1 & s

# print(new_set)
# print(s3)
def number_of_unique_characters(str):
    s = set()
    for char in str:
        s.add(char)
    return len(s)


def number_of_vowels(str):
    s = {'a', 'e', 'i','o' , 'u'}
    for i in str:
        s.discard(i)
    return 5 - len(s)



str = 'programming'
res = number_of_unique_characters(str)
answer = number_of_vowels(str)
print(res)
print(answer)
