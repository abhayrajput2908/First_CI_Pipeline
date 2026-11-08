
def set_intersection(first, second):
    return sorted(set(first) & set(second))


if __name__ == "__main__":
    first = list(map(int, input("Enter the first list of numbers: ").split()))
    second = list(map(int, input("Enter the second list of numbers: ").split()))

    print("Intersection:", set_intersection(first, second))
