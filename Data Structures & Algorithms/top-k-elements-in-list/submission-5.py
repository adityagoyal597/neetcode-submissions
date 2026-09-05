class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for num in nums:
            count[num]=1+count.get(num,0)

        minHeap=[]

        for num in count.keys():
            heapq.heappush(minHeap,(count[num],num))

            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        result=[]

        for freq,num in minHeap:
            result.append(num)
        
        return result