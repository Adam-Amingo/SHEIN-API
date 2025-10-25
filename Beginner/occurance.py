####1111111111111111111111
# def remove_all_occurance(str , ch):
    
#     res = ""
#     for char in str :
#         if (char != ch ):
#             res = res + char
    
#     return res

#222222222222222222222222222222222

# def remove_all_occurance(str , ch):
#     temp_list = str.split(ch)
#     return ''.join(temp_list)

# str = 'Welcome to python course'
# print(remove_all_occurance(str , 'o'))


#3333333333333333333333
def convert_string_into_camel_case(str):
    res = str[0].upper()
    n = len(str)
    for i in range(1,n):
        if(str[i - 1] == " "):
            res = res + str[i].upper()
        else:
            res = res + str[i]
    
    return res


def convert_string_into_capitalize(str):
    temp_list = str.split("")
    for i in range (len(temp_list)):
        temp_list[i] = temp_list[i].capitalize()
    return " ".join(temp_list)

str = "Hi there i am amingo"
print(convert_string_into_camel_case(str))
convert_string_into_capitalize(str)

