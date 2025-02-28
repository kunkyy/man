import sys

def decimal_to_hex(decimal_value):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input provided. Please provide a decimal number as an argument.")
        sys.exit(1)  # Exit with an error code

    try:
        decimal_value = int(sys.argv[1])  # Ensure input is an integer
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: Invalid input. Please provide a valid integer.")
        sys.exit(1)  # Exit with an error code
