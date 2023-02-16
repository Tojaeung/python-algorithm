# 투포인터 이용

from typing import List


def twoSum(nums: List[int], target: int) -> List[int] | None:
    left, right = 0, len(nums) - 1

    # 조건이 true가 될때까지 계속 진행
    while not left == right:
        # 왼쪽 포인터를 오른쪽으로 이동
        if nums[left] + nums[right] < target:
            left += 1
        # 오른쪽 포인터를 왼쪽으로 이동
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# 테스트 케이스
# nums = [2, 7, 11, 15]
# target = 9

# 두번째 케이스에서 오류난다.
# 주어진 nums 리스트가 정렬 상태가 아니다(투포인터 방법 X)
# sort()로 정렬하면 인덱스 구조가 깨져버림...
nums = [2, 3, 4]
target = 6

# nums = [3, 3]
# target = 6
print(twoSum(nums, target))
