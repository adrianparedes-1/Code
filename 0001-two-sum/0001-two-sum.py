
class Solution(object):
    def operation(self, current, target, hashmap):
        temp = target - current
        for i in range(len(hashmap)):
            if temp == hashmap[i]:
                return hashmap[i]
        return None  # Return None if no match is found

    def twoSum(self, nums, target):
        hashmap = dict(enumerate(nums))  # Keys are the indices of the values
        values = list(hashmap.values())  # Convert hashmap values to a list
        
        for j in range(len(values)):
            answer = self.operation(values[j], target, values)
            if answer is not None:
                index = values.index(answer)  # Find the index of answer in values
                if index != j:
                    return [j, index]
        
        return []  # Return an empty list if no solution is found
