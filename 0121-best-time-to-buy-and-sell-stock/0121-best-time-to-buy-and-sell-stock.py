class Solution(object):
    def maxProfit(self, prices):
        """
this problem is asking us to choose the two indices with the largest difference between their values. This will ensure maximum profit. 

The second index needs to be after the first index, and its value must also be larger than the first's.

plan:

1st value: likely the smallest value in the array
2nd value: largest value in the array after first


edge case: if the smallest value is the last value in the array, then we return 0 because any trade would result in a loss.


1. iterate through every value in the array and store the smallest value and its index in a variable.
2. same  thing but with the largest value that has a larger index than the smallest value.
3. Return largest - smallest

        """
        small = prices[0]
        total = 0
        index1 = 0
        index2 = 0

        for index, value in enumerate(prices):
            if value <= small:
                print("small value: ", value)
                small = value
                index1 = index
                print("index 1: ,", index1)
            
            total = max(total, value - small)
            
        return total


        