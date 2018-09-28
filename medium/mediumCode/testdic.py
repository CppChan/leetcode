from collections import Counter
class Bigram:

    def __init__(self, data):
        # Set up data structures here
        self.word_dic = {}
        # Process the input
        for sentence in data:
            # TODO: Process each sentence independently
            for i in range(len(sentence)-1):
                if not self.word_dic.has_key(sentence[i]): self.word_dic[sentence[i]] = []
                self.word_dic[sentence[i]].append(sentence[i+1])
        for item in self.word_dic.iteritems():
            following_dic, all = Counter(item[1]),0
            for following in following_dic.iteritems():
                all+=following[1]
            following_dic[1]=all
            self.word_dic[item[0]]=following_dic

    def prob(self, context, word):
        if not self.word_dic.has_key(context): return "Crash"
        context_dic = self.word_dic[context]
        if not context_dic.has_key(word): return "Crash"
        return float(context_dic[word])/float(context_dic[1])

if __name__=="__main__":
    b = Bigram([['the', 'quick', 'fox'],
        ['the', 'quick', 'jaguar'],
        ['the', 'slow', 'dog']])
    print b.prob("slow","dog")
