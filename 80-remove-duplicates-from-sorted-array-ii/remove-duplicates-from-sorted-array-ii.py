# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:

        
#         if len(nums) <= 2:
#             return len(nums)
        
#         pointer = 2
#         for i in range(pointer,len(nums)):
#             if nums[i] != nums[pointer-2]:
                
#                 nums[pointer] = nums[i]
#                 pointer += 1
#         return pointer



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        k = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] <= 2:
                nums[k] = num
                k += 1
        return k




   

          



           
                    
