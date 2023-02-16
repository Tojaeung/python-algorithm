# in 연산으로 구하기
# 시간복잡도 n^2로 풀이1과 같지만 in탐색이 더 빠름

from typing import List


def twoSum(nums: List[int], target: int):
    for i, v in enumerate(nums):
        num = target - v
        if num in nums[i + 1 :]:  # in을 이용한 탐색은 빠르다 !!
            return [i, nums[i + 1 :].index(num) + i + 1]


nums = [2, 7, 11, 15]
target = 26

print(twoSum(nums, target))
