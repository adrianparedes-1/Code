
class Solution(object):   
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        if the current number is less than the next, subtract current from next. if not, just add current
        
        edge case: check for out of range error.
        """
        # roman_to_int = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        def roman_to_int(c):
            if c == 'I':
                return 1
            elif c == 'V':
                return 5
            elif c == 'X':
                return 10
            elif c == 'L':
                return 50
            elif c == 'C':
                return 100
            elif c == 'D':
                return 500
            elif c == 'M':
                return 1000
            else:
                return 0 
        total = 0
        
        for i in range(len(s)):
            print(roman_to_int(s[i]))
            if i + 1 < len(s) and roman_to_int(s[i]) < roman_to_int(s[i + 1]):
                total -= roman_to_int(s[i])
            else:
                total += roman_to_int(s[i])
        
        return total
            
        