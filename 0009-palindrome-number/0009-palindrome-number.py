class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = list(map(int, str(x)))
        print(n)
        i = 0
        j = len(n) - 1
        print(i)
        print(j)
        while i < j:
            if n[i] == n[j]:
                i+=1
                j-=1
                print(i)
                print(j)
            else:
                return False
        
        return True

