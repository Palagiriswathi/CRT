class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        d = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                d[s] = d.get(s, 0) + 1

        cows = 0
        for s, g in zip(secret, guess):
            if s != g and d.get(g, 0) > 0:
                cows += 1
                d[g] -= 1

        return f"{bulls}A{cows}B"
         