class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        temp=[]
        n=len(nums)
        if len(nums)==1:
            return 1
        elif nums==[]:
            return 0
        
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                count+=1
                temp.append(count)
            else:
                temp.append(count)
                count=0
        res=max(temp)+1
        return res
