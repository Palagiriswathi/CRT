class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        def s(num):
            ans = 0
            for ch in num:
                ans = ans * 10 + ord(ch) - ord('0')
            return ans

        def t(st):
            res = ""

            while st > 0:
                a = st % 10
                st = st // 10
                res = chr(ord('0') + a) + res

            return res

        return t(s(num1) * s(num2))