# 풀이3 for 구문 2개를 1개로 개선

from typing import List


def twoSum(nums: List[int], target: int) -> List[int] | None:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 테스트 케이스
nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
nums = [3, 3]
target = 6
print(twoSum(nums, target))
