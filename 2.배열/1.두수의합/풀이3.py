# https://leetcode.com/problems/two-sum/
# 첫번쨰 수를 뺸 결과 키조회 (딕셔너리의 해쉬테이블 사용)
# 시간복잡도 O(1)

from typing import List


def twoSum(nums: List[int], target: int) -> List[int] | None:
    nums_map = {}

    # 키와 값을 바꿔 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫번째 수를 뺸 결과를 조회
    for i, num in enumerate(nums):
        # 같은 리스트요소를 가지면 오류나기 때문에 조건 처리해준다.
        # i != nums_map[target - num]
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 테스트 케이스
nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
nums = [3, 3]
target = 6
print(twoSum(nums, target))
