"""
Microsoft 1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

# First Attempt, In Progress:
class Solution(object):
    def maxVowels(self, s, k):
        n = len(s)
        beg = 0
        end = k
        max_count = 0
        vowels='aeiou'
        while end < n:
            sub = s[beg:end]
            for l in sub:
                count=0
                if l in vowels:
                    count=count+1
            if count < max_count:
                max_count=count
            beg+=1
            end+=1
        return max_count
