#print("hello world")
my_str = 'bhavana'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("The string is not a palindrome")
else:
    print("the string is a palindrome")
