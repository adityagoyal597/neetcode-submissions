class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache={}

        def dfs(i):
            if i==len(days):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i]=float("inf")
            j=i

            for duration, cost in zip([1,7,30],costs):
                while j<len(days) and days[j]<days[i]+duration:
                    j+=1
                cache[i]=min(cache[i],cost+dfs(j))
            
            return cache[i]
        
        return dfs(0)
        