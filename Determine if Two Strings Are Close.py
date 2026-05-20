class Solution:
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False

        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        return sorted(freq1.values()) == sorted(freq2.values())
