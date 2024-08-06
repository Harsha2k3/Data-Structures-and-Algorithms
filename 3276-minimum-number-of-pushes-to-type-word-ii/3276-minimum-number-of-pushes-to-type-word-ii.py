class Solution:
    def minimumPushes(self, word: str) -> int:

       chr = sorted(Counter(word).values(), reverse = True)

       return (sum(chr[:8]) + 2 * sum(chr[ 8:16]) + 3 * sum(chr[16:24]) + 4 * sum(chr[24:]))