# function to check whether a string is a palindrome

# def is_palindrome(str):
#     return str == str[::-1]

def is_palindrome(str):
    len_str = len(str)

    for i in range(0, len_str // 2):
        if str[i] != str[len_str - i - 1]:
            return False

    return True

print(is_palindrome("aabbbbaa"))
