# https://leetcode.com/problems/group-anagrams/

import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # key가 없을시 빈 list 삽입
    anagrams = collections.defaultdict(list)

    # sort()와 sorted()의 차이
    for word in strs:
        anagrams[str(sorted(word))].append(word)
        # anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
