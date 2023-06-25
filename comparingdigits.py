# Comparing Digits
n = int(input())
if n > 25:
    n_string = str(n)
    first_digit = n_string[0]
    second_digit = n_string[1]
    first_digit = int(first_digit)
    second_digit = int(second_digit)
    if first_digit > second_digit:
        print(True)
    else:
        print(False)
else:
    print(False)
    