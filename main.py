def is_multiple_of_three(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value % 3 == 0

def find_binary_multiples(lines):
    result = []
    for line in lines:
        line = line.strip()
        if is_multiple_of_three(line):
            result.append(line)
    return result

# Пример использования:
input_strings = [
    "110",      # 6 (2^2 + 2^1 = 4 + 2)
    "1010",     # 10 (2^3 + 2^1 = 8 + 2)
    "1111",     # 15 (2^3 + 2^2 + 2^1 + 2^0 = 8 + 4 + 2 + 1)
    "1001",     # 9 (2^3 + 2^0 = 8 + 1)
    "1100"      # 12 (2^3 + 2^2 = 8 + 4)
]

result = find_binary_multiples(input_strings)

print("Строки с двоичной записью числа, кратного 3:")
for line in result:
    print(line)