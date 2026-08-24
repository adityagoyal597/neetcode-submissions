class TimeMap:

    def __init__(self):
        self.store={} #string:[[val,timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.store.get(key,[])

        L,R=0,len(values)-1
        while L<=R:
            mid=(L+R)//2
            if values[mid][1]<= timestamp:
                res= values[mid][0]
                L=mid+1
            else: # values[mid][1]>timestamp
                R=mid-1
        
        return res

