class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]

        L,R=0,0
        queue=deque()

        while R<len(nums):
            while queue and nums[queue[-1]]<nums[R]:
                queue.pop()
            queue.append(R)

            if L>queue[0]:
                queue.popleft()
            
            if(R+1)>=k:
                output.append(nums[queue[0]])
                L+=1
            R+=1
        
        return output