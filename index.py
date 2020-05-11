from number_constants import number_constants


def number_to_string(input):
    if input > 20:
        if input < 100:
            temp = input // 10
            temp = temp * 10
            word = number_constants[temp]
            res = input - temp
            word = word + " " + number_constants[res]

            return word
    else:
        return number_constants[input]
