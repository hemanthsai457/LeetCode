class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        return [n for num, i in counter.most_common(k)]
        
