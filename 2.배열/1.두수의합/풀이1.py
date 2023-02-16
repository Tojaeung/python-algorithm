# 리트코드 1번 두수의 합
# 브루트포스 (무치별 대입방식)
# 시간복잡도 n^2

from typing import List


def twoSum(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
