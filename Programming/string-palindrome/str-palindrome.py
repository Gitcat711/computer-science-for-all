# this program deals with string palindrome
def is_palindrome(string):
    if string == u''.join(reversed(string)):
        return True
    else:
        return False

print(is_palindrome("civic"))


