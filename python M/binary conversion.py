def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal
def decimal_to_octal(decimal):
    octal = oct(decimal)
    return octal
binary,num = input("enter a binary number: ")
decimal_result = binary_to_decimal(binary_num)
print(f"Decimal equivalent of {binary_num}: {decimal_result}")
octal_result = decimal_to_octal(decimal_result)
print(f"Octal equivalent of {decimal_result}: {octal_result}")
