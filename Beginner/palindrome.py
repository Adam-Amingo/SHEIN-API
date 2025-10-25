def isPalindrome(str):
    n = len(str)

    for i in range (n // 2):
        if(str[i] != str[n - 1 - i]):
            return False
    return True

str = 'madam'
res = isPalindrome(str)
print(res)

