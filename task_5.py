def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    most = numbers[0]

    for number in numbers:
        if counts[number] > counts[most]:
            most = number

    return most

print(most_frequent([4, 7, 7, 4]))    
