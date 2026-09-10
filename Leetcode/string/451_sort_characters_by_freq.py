# TC= O(n + k log k) SC=O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for key, val in sorted_chars:
            result += key * val
        return result
