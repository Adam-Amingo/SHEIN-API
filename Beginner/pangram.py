def check_if_pangram(str):
    str= str.lower()
    s = set()
    for i in str:
        if (i.isalpha()):
            s.add(i)
    return len(s) == 26


str = 'a$ +=bgt645'
res = check_if_pangram(str)
print(res)