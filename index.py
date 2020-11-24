from number_constants import number_constants


def number_to_string(input):
    numbers = [n for n in str(input)]
    convert_numbers = []
    for i, n in zip(reversed(range(len(numbers))), numbers):
        if 10 ** i >= 100:
            convert_numbers.append(n)
        convert_numbers.append(int(n) * 10 ** i)
    words = [number_constants[int(n)] for n in convert_numbers]
    return ' '.join(words)
