class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)-1
        sum = 0
        for i in digits:
            sum = sum + (i*(10**l))
            l -= 1
        return list(str(sum + 1))