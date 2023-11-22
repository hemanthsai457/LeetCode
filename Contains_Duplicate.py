class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                return True
        return False
