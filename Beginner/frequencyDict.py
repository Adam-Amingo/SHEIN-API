# def find_frequency(str):
#     dc = {}
#     for char in str:
#         if char in dc :
#             dc[char] = dc[char] + 1
#         else :
#             dc[char] = 1 

#     return dc


def find_frequency(str):
    dc = {}
    for char in str:
        dc[char]= dc.get(char , 0 ) + 1
    return dc

def find_duplicate(dc):
    arr = []
    for  key , val in dc.items():
        if val > 1 :
            arr.append(key)
    return arr


str = 'programming'
dc = find_frequency(str)
res = find_duplicate(dc)
print(res)