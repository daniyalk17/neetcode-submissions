class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val, index

        for indx, val in enumerate(nums): 
            diff = target - val
            
            if target - val in hashMap: 
                return [hashMap[diff], indx]
            else: 
                hashMap[val] = indx

        