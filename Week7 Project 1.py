def mean(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    """Returns the median of a list of numbers."""
    if not numbers:
        return 0

    numbers = sorted(numbers)
    length = len(numbers)
    mid = length // 2

    if length % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2


def mode(numbers):
    """Returns the mode of a list of numbers."""
    if not numbers:
        return 0

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    for num in counts:
        if counts[num] == max_count:
            return num


def main():
    """Tests the statistical functions."""
    data = [1, 2, 2, 3, 4, 5]

    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))


if __name__ == "__main__":
    main()
