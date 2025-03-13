class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str


        U: the problem is asking us to create function that merges two strings by alternating characters from each string.

        two strings -- start populating from word1 then word2
        until there are no characters left in string

        P: 1. loop that selects a character from each string at position i
        2. append each character
        3. error handling (if character is null and it is less than the length of the longest string ---> skip it)
        4. return new string once length of both words together is parsed
        """
        merged = []

        for i in range(len(word1 + word2)):
            try:
                merged.append(word1[i])
            except IndexError:
                pass
            try:
                merged.append(word2[i])
            except IndexError:
                pass
                
        merged_s = "".join(merged)
        return merged_s
        