# https://leetcode.com/problems/most-common-word/

import collections
import re
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]):
    # 문자열 이외의 것 공백처리
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]
    # print(words) # words가 어떻게 만들어지는지 과정

    counts = collections.Counter(words)
    # print(counts) # Count 딕셔너리 확인 (key = 요소, value = 카운트)

    # Counter 딕셔너리에서 가장 카운트가 많은 1개
    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))
