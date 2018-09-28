class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        if word1 == word2:
            return self.find1(words, word1)
        else:
            return self.find2(words, word1, word2)

    def find1(self, words, word):
        pre = None
        res = float('inf')
        for i in range(len(words)):
            if words[i] == word:
                if pre == None:
                    pre = i
                else:
                    if i - pre < res: res = i - pre
                    pre = i
        return res

    def find2(self, words, word1, word2):
        pending, now, res = None, None, float('inf')
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if pending == None:
                    if words[i] == word1:
                        pending = word2
                    else:
                        pending = word1
                elif words[i] == pending:
                    if i - now < res: res = i - now
                    if words[i] == word1:
                        pending = word2
                    else:
                        pending = word1
                now = i
        return res