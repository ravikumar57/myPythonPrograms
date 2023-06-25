a = input()
l = len(a)
first_letter = a[0]
last_letter = a[l-1]
remaining_string = "*" * (l-2)
result = first_letter + remaining_string +last_letter
print(result)   