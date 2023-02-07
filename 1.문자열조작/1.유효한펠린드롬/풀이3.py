# 슬라이싱 이용


import re


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub("[a-z0-9]", "", s)

    print(s)
    print(s[::-1])

    # 슬라이싱으로 s 뒤집기
    return s == s[::-1]


s = str(input())
print(isPalindrome(s))
