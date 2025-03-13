class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

    U: the problem is asking to validate whether a string is a palindrome or not. A palindrome is a string that reads the same forwards and backwards after removing:
    1. capital letters
    2. non-alphanumeric characters

    P: First we need to change all capital letters to lowercase. We can use lower() function to do this.
    Secondly, we need to remove everything that is not an alphanumeric character. For now, I'm just going to account for letters and we will see the test cases to see if there are any numbers to account for. We can remove the non-alphanumeric characters with slicing. It is probably the easiest method to understand. 

    iterate through string:
    if char is capital:
        change it to lower
    if char is not a letter:
        slice string from char index - 1 to char index + 1
        """
        s = s.lower()
        for i in s:
            if i.isalnum() == False:
                s = s.replace(i,"")
      
        if s == s[::-1]:
            return True
        else:
            return False