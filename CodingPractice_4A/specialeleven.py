# Special Eleven
n = int(input())
remainder = n % 11
condition = (remainder == 0) or (remainder == 1)
if condition:
    print("Special Eleven")
else:
    print("Normal Number")