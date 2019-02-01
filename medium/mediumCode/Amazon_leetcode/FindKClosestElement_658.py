from collections import deque
class Solution(object):
    def findClosestElements(self, arr, k, x):
        i,j, closest= 0, len(arr)-1, None
        while i<j-1:
            mid = (i+j)/2
            if arr[mid]==x:
                closest = mid
                break
            elif arr[mid]<x:i=mid
            else: j = mid
        if closest==None and abs(arr[i]-x)<=abs(arr[j]-x):closest =i
        elif closest==None and abs(arr[i]-x)>abs(arr[j]-x): closest = j
        i,j = closest, closest+1
        while k>0:
            if (j>=len(arr) and i>=0) or(i>=0 and abs(arr[i]-x)<=abs(arr[j]-x)): i-=1
            elif (i<0 and j<len(arr)) or (j<len(arr) and abs(arr[i]-x)>abs(arr[j]-x)):j+=1
            k-=1
        return arr[i+1:j]