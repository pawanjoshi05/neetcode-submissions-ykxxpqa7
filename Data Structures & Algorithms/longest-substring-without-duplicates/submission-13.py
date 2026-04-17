class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        count = 0
        map = {}

        while (j < len(s)):
            if (s[j] not in map):
                map[s[j]] = 1
                count = max(count, j - i + 1)
                j += 1
            else:
                # duplicate mila → remove until valid
                while (s[j] in map):
                    map.pop(s[i])
                    i += 1

                # ab window valid ho gayi
                map[s[j]] = 1
                count = max(count, j - i + 1)
                j += 1

        return count