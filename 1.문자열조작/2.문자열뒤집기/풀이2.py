# 파이썬 다운 방식

from typing import List


def reverseString(s: List[str]) -> List[str]:
    s.reverse()  # reverse 메서드로 스왑
    return s

    # s = s[::-1] # 리스트에 슬라이싱 사용가능
    # return s


s = list(input())
print(reverseString(s))
