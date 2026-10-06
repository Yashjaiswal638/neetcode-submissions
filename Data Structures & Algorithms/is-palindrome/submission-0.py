class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum() or char == " ")
        s = s.replace(" ", "")
        s1 = s[::-1]
        if s1.lower() == s.lower():
            return True
        return False