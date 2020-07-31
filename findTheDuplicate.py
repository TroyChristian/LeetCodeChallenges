class Solution:
    def findDuplicate(self, nums) -> int:
        numbers_checked = set()
        for num in nums:
            if num in numbers_checked:
                return num

            numbers_checked.add(num)
            

a = Solution()
print(a.findDuplicate([1,3,4,2,2]))
print(a.findDuplicate([3,1,3,4,2]))
      
