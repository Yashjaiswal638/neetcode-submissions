class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in nums:
        #     k = 0
        #     for j in nums:
        #         if i == j:
        #             k = k+1
        #     if k==2:
        #         return True
        # return False
        
        random = set()
        for num in nums:
            if num in random:
                return True
            random.add(num)
        return False