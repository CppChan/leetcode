from heapq import heappush, heappop

# If max height changes, record [x, height] in res


class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        # a = {(R, 0, 0) for _, R, _ in buildings}
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort() # after that is a sorted array [(L,-H,R),(R,0,0)....]

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]] #[x, height]
        live = [(0, float("inf"))] # [height, right]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: # 当 存活最高building的right <= 当前竖线的x
                heappop(live) # 去掉存活的最高building
            if negH:# 如果 是building， 有高度
                heappush(live, (negH, R)) # push （高度， 结束点）
            if res[-1][1] != -live[0][0]: # if res 最后的高度 ！= 存活的building的最高高度， 什么时候会发生这个（当刚刚pop掉一个失效了的live 最高高度building， 或者刚push一个最高高度的building
                res += [ [pos, -live[0][0]] ] # res 加入 （当前x，存活的building的最高高度）
        return res[1:]


#查看手机照片 2018／10／28

if __name__=="__main__":

    s = Solution()
    s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])