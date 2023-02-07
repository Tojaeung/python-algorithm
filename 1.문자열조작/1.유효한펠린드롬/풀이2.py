# 덱 이용

import collections
from typing import Deque


def isPalindrome(s: str) -> bool:
    strs: Deque[str] = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


s = str(input())
print(isPalindrome(s))
