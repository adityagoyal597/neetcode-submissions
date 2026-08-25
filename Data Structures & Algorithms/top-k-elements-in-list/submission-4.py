class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} # num:frequecy
        for num in nums:
            count[num]=1+count.get(num,0)
        
        minHeap=[]

        for num in count.keys():
            heapq.heappush(minHeap,(count[num],num)) # (freq,num)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
            
        res=[]
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
