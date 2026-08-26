class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}

        for task in tasks:
            count[task]=1+count.get(task,0)
        
        maxHeap=[-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time=0
        # queue stores the tasks currently being cooldown
        queue=deque() # [remaining freq,time when available]

        while maxHeap or queue:
            time+=1

            if not maxHeap:
                time=queue[0][1]
            else:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt,time+n])
            
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time
