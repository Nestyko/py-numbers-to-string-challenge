from number_constants import number_constants


def number_to_string(input):
    numbers = [n for n in str(input)]
    convert_numbers = []
    for i, n in zip(reversed(range(len(numbers))), numbers):
        if 10 ** i >= 100:
            convert_numbers.append(n)
        if number_constants.get(int(n) * 10 ** i) is None:
            convert_numbers.append(10 ** i)
        else:
            convert_numbers.append(int(n) * 10 ** i)
    words = [number_constants[int(n)] for n in convert_numbers if number_constants[int(n)] != "zero"]
    return ' '.join(words)
