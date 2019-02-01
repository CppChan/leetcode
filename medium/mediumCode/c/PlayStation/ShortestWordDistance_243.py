class Solution(object):
    def shortestDistance(self, words, word1, word2):
        if word1 == word2: return 0
        pos, shortest = {}, [float('inf')]
        cur, other = None, None
        for i in range(len(words)):
            if words[i] in (word1, word2):
                if words[i] == word1:
                    cur, other = word1, word2
                else:
                    cur, other = word2, word1
                self.check(i, cur, other, pos, shortest)
        return shortest[0]

    def check(self, i, cur, other, pos, shortest):
        if other in pos: shortest[0] = min(shortest[0], i - pos[other])
        pos[cur] = i