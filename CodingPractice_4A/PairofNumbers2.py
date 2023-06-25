# Pair of Numbers - 2:
a=int(input())
b=int(input())
C1=(a%3 == 0) and (b%3 == 0)
C2=(a%12 ==0) or (b%12 == 0)
if C1 and C2:
    print("Pair")
else:
    print("Not a Pair")