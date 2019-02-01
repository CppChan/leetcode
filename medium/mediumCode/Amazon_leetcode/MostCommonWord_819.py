import re
from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        word = re.split('[!,?.;\'\ ]', paragraph)
        word_count, max_count, res= defaultdict(lambda: 0), 0, None
        banned = set(banned)
        for i in range(len(word)):
            if len(word[i])==0:continue
            temp = word[i].strip().lower()
            if temp in banned:continue
            word_count[temp]+=1
            if word_count[temp]>max_count:
                max_count=word_count[temp]
                res = temp
        return res