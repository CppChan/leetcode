# record the last index of each element
# then traverse again,


class Solution(object):
    def partitionLabels(self, S):
        if not S or len(S) == 0:
            return None
        lasts = dict()
        for i in range(len(S)):
            lasts[ord(S[i]) - ord("a")] = i
        start = 0
        last = 0
        sizes = list()
        for i in range(len(S)):
            last = max(last, lasts[ord(S[i]) - ord("a")]) # "last" is the earliest index to finish this segment list
            if last == i: # S[i] and S[before i] will not appear in future segment
                sizes.append(last - start + 1)
                start = last + 1
        return sizes


s = Solution()
print s.partitionLabels("ababcbacadefegdehijhklij")
print list("ababcbacadefegdehijhklij")