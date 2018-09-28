from Queue import PriorityQueue
from Queue import Queue
import heapq
from collections import deque

#1.PriorityQueue: used heapq to realize:

#heapq.heappush(heap, item)
#Push the value item onto the heap, maintaining the heap invariant.

#heapq.heappop(heap)
#Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

#heapq.heappushpop(heap, item)
#Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

#New in version 2.6.

#heapq.heapify(x)
#Transform list x into a heap, in-place, in linear time.


#2.Queue implementation: from collections import deque
#

#3. Stack implementaion: use list's pop() append()  len()  [-1] method

class Skill(object):##compare class!!!!!!!
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    def __cmp__(self,other):#
        #call global(builtin) function cmp for int
        return cmp(self.description, other.description)#add '-' to change order

    # def __str__(self):
    #     return '(' + str(self.priority)+',\'' + self.description + '\')'



if __name__ == "__main__":

    heap  = []
    heapq.heappush(heap,Skill(5,'abc'))
    heapq.heappush(heap,Skill(10,'abb'))
    heapq.heappush(heap,Skill(1,'bcc'))
    heapq.heappush(heap,Skill(9,'bca'))

    while heap:
        print heapq.heappop(heap).priority
    print("*******************")

    b =[5,2,9,4]
    a = PriorityQueue()
    heapq.heappush(b, 3)
    heapq.heapify(b) #once heapify, then the heap will maintain the order forever
    print heapq.heappop(b)
    print heapq.heappop(b)
    heapq.heappush(b,1)
    print b[0]
    print b[1]
    print len(b)

    print("*******************")

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print heapq.nlargest(3, nums)
    print nums

    a = deque([])
    a.append(6)
    a.append(5)
    a.append(4)
    print a
    print a.pop()
    print a.popleft()
    print a[0]
    print len(a)




