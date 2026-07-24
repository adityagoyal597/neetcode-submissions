class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for num in numSet:
            # checking if the left neighour doesn't exist for the start of the sequence
            if(num-1) not in numSet:
                # num can be the start of the sequence
                length=0
                while(num+length) in numSet:
                    length+=1
                longest=max(longest,length)
        return longest