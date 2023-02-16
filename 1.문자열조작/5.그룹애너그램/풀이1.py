# https://leetcode.com/problems/group-anagrams/

import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # key가 없을시 빈 list 삽입
    anagrams = collections.defaultdict(list)

    # sort()와 sorted()의 차이
    for word in strs:
        """
        words = [
            "토재웅",
            "이게나다",
            "나다호다",
        ]

        print(str(sorted(words)))  # ['나다호다', '이게나다', '토재웅']
        print("".join(sorted(words)))  # 나다호다이게나다토재웅
        """

        anagrams["".join(sorted(word))].append(word)
        # anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
