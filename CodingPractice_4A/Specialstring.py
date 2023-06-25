# Special String:
s = input()
C1 = s[0]+s[1]+s[2]
C2 = int(s[3:])
A1 = "NXT"
A2 = (C2%2 == 0) or (C2%7 == 0)
if C1 == A1 and A2:
    print("Special String")
else:
    print("Not a Special String")