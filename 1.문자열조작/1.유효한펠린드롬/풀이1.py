# 리스트 이용

import sys
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def isPalindrom(s: str) -> bool:
    strs: List[str] = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


s = str(input())
print(isPalindrom(s))
