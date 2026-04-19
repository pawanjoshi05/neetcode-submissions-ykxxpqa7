class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i = 0
        j = 0
        count = {}
        max_frq = 0
        answer = 0
        n = len(s)

        while j < n:

            key = s[j]

            if key in count:
                count[key] += 1
            else:
                count[key] = 1

            if count[key] > max_frq:
                max_frq = count[key]

            window_len = j - i + 1

            if (window_len - max_frq) <= k:

                if window_len > answer:
                    answer = window_len

                j += 1

            else:
                while (window_len - max_frq) > k:

                    left_key = s[i]
                    count[left_key] -= 1

                    i += 1
                    window_len = j - i + 1

                if window_len > answer:
                    answer = window_len

                j += 1

        return answer