class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        occurrences = list(freq.values())

        return len(occurrences) == len(set(occurrences))
        
