class TrieTreeNode(object):
    def __init__(self):
        self.chiledren=[None]*26
        self.count = 0
        self.isEnd = False

class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()

    def add(self, word):
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord("a")
            if not cur.children[index]:
                cur.children[index] = TrieTreeNode()
            cur.count+=1
            cur = cur.children[index]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord("a")
            if not cur.children[index]:
                return False
            cur = cur.chiledren[index]
        return True

    def deleteWord(self, word):
        self.deleteHelper(self.root, word, 0)

    def deleteHelper(self, root, word, index):
        if index == len(word):
            root.isEnd = False
            return
        i = ord(word[index]) - ord("a")
        self.deleteHelper(root.children[i],word,index+1)
        root.count-=1
        if root.children[i].count == 0:
            root.children[i]=None
        return
