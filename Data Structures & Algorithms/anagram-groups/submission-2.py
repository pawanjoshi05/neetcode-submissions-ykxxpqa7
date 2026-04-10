from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        
        # used[i] tells whether strs[i] is already grouped or not
        used = [False] * n
        
        # final answer
        output = []

        # Step 1: iterate over each word
        for i in range(n):
            
            # if already grouped, skip
            if used[i]:
                continue

            # Step 2: start a new group with current word
            temp = [strs[i]]
            used[i] = True   # mark current word as used

            # Step 3: compare this word with all remaining words
            for j in range(i + 1, n):
                
                # only check if not already used
                if not used[j]:
                    
                    # Step 4: check if both are anagrams
                    # by sorting both words and comparing
                    if sorted(strs[i]) == sorted(strs[j]):
                        
                        # Step 5: if anagram, add to group
                        temp.append(strs[j])
                        
                        # mark as used so it is not used again
                        used[j] = True

            # Step 6: add this group to final output
            output.append(temp)

        # Step 7: return all groups
        return output