def palindrome(s):
    return s == s[::-1]

word = input("String: ")

if palindrome(word):
    print(f'"{word}" is a palindrome')
else:
    print(f'"{word}" is not a palindrome')
