# Last updated: 7/19/2025, 2:25:38 PM
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        b=Counter(words)
        sorg=sorted(b.items(),key=lambda x:(-x[1], x[0]))
        sorg=sorg[:k]
        return [n[0] for n in sorg]