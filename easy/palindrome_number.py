"""Given an integer x, return true if x is palindrome integer"""


def isPalindrome(self, x: int) -> bool:
    x = str(x)           # convert x to a string
    return x == x[::-1]  # reverse x to read the same backwards
