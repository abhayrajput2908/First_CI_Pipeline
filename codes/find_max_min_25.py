
def find_max_min(numbers):
    if not numbers:
        return None, None

    return max(numbers), min(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    maximum, minimum = find_max_min(numbers)

    if maximum is None:
        print("The list is empty.")
    else:
        print("Maximum:", maximum)
        print("Minimum:", minimum)
