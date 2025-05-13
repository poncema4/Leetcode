class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for ii, i in enumerate(s):
            res += roman[i]
            if ii + 1 != len(s) and roman[s[ii + 1]] > roman[s[ii]]:
                res -= 2 * roman[s[ii]]
        return res