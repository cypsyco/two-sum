from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    
    for i, num in enumerate(nums):
        pair = target - num
        if pair in num_dict:
            return [num_dict[pair], i]
        num_dict[num] = i
