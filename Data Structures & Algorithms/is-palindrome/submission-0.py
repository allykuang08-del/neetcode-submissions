class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        import string

        str1 = s.lower()
        str2 = str1.replace(" ", "")
        str3 = str2.translate(str.maketrans("", "", string.punctuation))

        if str3 == str3[::-1]:
            return True
        else:
            return False