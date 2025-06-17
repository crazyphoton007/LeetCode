class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0
        reader = 0
        n = len(nums)
        i = 0

        while (reader < n):
 
            if nums[reader] == val:
                reader = reader + 1

            else:
                nums[writer] = nums[reader]
                reader = reader + 1
                writer = writer + 1
        

        return writer





        
        