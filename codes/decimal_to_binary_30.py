
def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    return bin(number)[2:]


if __name__ == "__main__":
    number = int(input("Enter a non-negative decimal integer: "))

    print("Binary representation:", decimal_to_binary(number))
