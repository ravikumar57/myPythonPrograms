# Two Digit Divisible Number:
n = input()
if len(n) == 2:
    n1 = int(n[0])
    n2 = int(n[1])
    n = int(n)
    condition = (n%n1 == 0) and (n%n2 == 0)
    if condition:
        print(n*2)
    else:
        print(n)
else:
    print("Provide 2 digits number only")