# Problem: Check palindrome

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))
