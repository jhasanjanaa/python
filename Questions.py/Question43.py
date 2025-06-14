'''
➡ Ek StringUtils class banao jisme ek static method is_palindrome(s) ho jo check kare ki s palindrome hai ya nahi.
➡ Ek aur static method count_vowels(s) likho jo s me vowels (a, e, i, o, u) count kare.
➡ Bina object banaye dono methods ko call karo.
'''

class StringUtils:
    @staticmethod
    def is_palindrome(s):
       return s == s[::-1]
    def count_vowels(s):
       return sum(1 for char in s.lower() if char in "aeiou")
              
print(StringUtils.is_palindrome("madam"))  # True ✅
print(StringUtils.is_palindrome("hello"))  # False ✅
print(StringUtils.count_vowels("hello"))   # 2 ✅
print(StringUtils.count_vowels("Sanjana")) # 3 ✅        