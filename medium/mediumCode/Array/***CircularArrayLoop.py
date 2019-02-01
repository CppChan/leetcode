class Solution(object):
    def circularArrayLoop(self, nums):
        for i in range(len(nums)):
            if not type(nums[i])==int or nums[i]%len(nums)==0:continue
            dir = True if nums[i]>0 else False
            j, mark= i, str(i)#use str(i) as decode way
            while True:
                if (nums[j]>0 and not dir) or (nums[j]<0 and dir) or nums[j]%len(nums)==0: break # wrong directoin or self loop detected
                nextindex = j+nums[j]
                if nextindex<0 or nextindex>=len(nums):nextindex%=len(nums) #new index
                if nums[nextindex]==mark: return True
                nums[j]=mark
                j = nextindex
        return False


s = Solution()

print s.circularArrayLoop([2,-1])