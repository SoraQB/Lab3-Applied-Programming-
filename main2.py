import re

regex = re.compile(r'^(1(01*0)*1|0)+$')

binary_numbers = [bin(i)[2:] for i in range(10000)]

count = 0;
errors = []

for binary_number in binary_numbers:
    decimal_number = int(binary_number, 2)

    if regex.match(binary_number):
        errors.append(decimal_number)
        count += 1;

print("Количество выведенных чисел", count)
print("Числа, кратные трем:", errors)


count_divisible_by_3 = sum(1 for binary_number in binary_numbers if int(binary_number, 2) % 3 == 0)

print("Количество чисел кратных 3:", count_divisible_by_3)
