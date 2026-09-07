class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = 1
        last = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            new_dp = (2 * dp - last[i]) % MOD

            last[i] = dp
            dp = new_dp

        return (dp - 1) % MOD