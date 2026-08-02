class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap=nums
        self.k=k
        heapq.heapify(self.minHeap) # list-> heap
        while len(self.minHeap)>k: # pop all the elements except k largest elements in the heap while mainting the heap properties
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # push the elemts in the heap to it's appropriate place
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k: # if the length ecxeeds the k then pop the elements except k largesgt elements in the array
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
