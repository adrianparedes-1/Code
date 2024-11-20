class Solution(object):
    
    def containsDuplicate(self, nums):
        dict = {}
        
        if len(nums) < 2:
            return False

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        print(dict)

        for key in dict:
            if dict[key] > 1:
                return True

        return False

        