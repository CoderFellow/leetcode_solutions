class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)  # Odd length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)  # Even length palindromes
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start : end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
