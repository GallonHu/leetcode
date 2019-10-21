class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for ind, val in nums:
            hash_map[val] = ind

        for ind1, val in nums:
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind2 != ind1:
                    return [ind1, ind2]