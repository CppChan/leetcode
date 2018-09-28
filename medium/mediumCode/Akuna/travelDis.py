import math

print math.sin(2*math.pi*30/360)

class Solution(object):
    def compute(self, lat1,long1,lat2,long2,):
        delta = abs(long1-long2)
        res = math.acos(math.sin(2*math.pi*abs(lat1)/360)*math.sin(2*math.pi*abs(lat2)/360)+math.cos(2*math.pi*abs(lat1)/360)
                        *math.cos(2*math.pi*abs(lat2)/360)*math.cos(2*math.pi*delta/360))
        return res*3963

if __name__=="__main__":
    s = Solution()
    print s.compute(41.836944, -87.684722, 40.7127, -74.0059)