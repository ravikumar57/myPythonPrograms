# LuckyNumber-2:
n = input()
if len(n) == 2:
    int_n = int(n)
    remainder = int_n % 9
    is_multipleof_9 = (remainder == 0)
    n_string = str(int_n)
    first_digit = int(n_string[0])
    second_digit = int(n_string[1])
    first_with_9 = (first_digit == 9)
    Second_with_9 = (second_digit ==9)
    any_digit_is_9 = first_with_9 or Second_with_9
    condition = any_digit_is_9 or is_multipleof_9
    if condition:
        print("Lucky Number")
    else:
        print("Unlucky Number")
else:
    print("Unlucky Number")
