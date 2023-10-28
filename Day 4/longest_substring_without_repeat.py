class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = right = 0
        n = len(s)
        length = 0
        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]]+1, left)
            hash_map[s[right]] = right
            length = max(length, right - left + 1)
            right += 1
        return length


sol = Solution()
sol.lengthOfLongestSubstring(s="abcabcbb")