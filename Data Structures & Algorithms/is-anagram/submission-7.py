class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # making a hashmap for both and then comparing both 
        
        if len(s) != len(t):   # ✅ crucial fix
            return False
        
        map1 = {}
        map2 = {}

        for i in s:
            curr = i
            map1[i] = map1.get(curr, 0) + 1

        for i in t:
            curr = i
            map2[i] = map2.get(curr, 0) + 1
        
        for key, value in map1.items():
            if (map2.get(key, 0) != value):
                return False
        
        return True