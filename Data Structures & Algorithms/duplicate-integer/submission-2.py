class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        random = set()
        for num in nums:
            if num in random:
                return True
            random.add(num)
        return False