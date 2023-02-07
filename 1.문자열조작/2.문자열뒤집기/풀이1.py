# 투포인터를 이용한 스왑

from typing import List


def reverseString(s: List[str]) -> List[str]:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


s = list(input())
print(reverseString(s))
