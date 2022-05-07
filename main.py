import math
n, k=input().split()
n, k=[int(n), int(k)]
s=n-k
symbol_Newtona=math.factorial(n)/(math.factorial(k)*math.factorial(s))
print(int(symbol_Newtona))