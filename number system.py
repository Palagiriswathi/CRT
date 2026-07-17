x = "151"
ans = 0
for ch in x:
    ans = ans * 10 + (ord(ch) - ord('0'))
print(ans)
print(type(ans))   

x = 152
res = ""

while x > 0:
    a = x % 10
    x //= 10
    res = chr(ord('0') + a) + res

print(res)