import heapq

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        score = {}
        for r in results:
            if r.id in score:
                score[r.id].append(r.score)
            else:
                score[r.id] = [r.score]
        answer = {}
        for id in score:
            answer[id] = sum(heapq.nlargest(5, score[id])) / 5.0
        return answer


s = Solution()
a = Record(1,100)
print s.highFive([a])