from number_constants import number_constants


def number_to_string(input):
    if input < 21:
        return number_constants[input]
    else:
        #dividir el número en sus partes (10) 143
        # 1*100 + 1*40 + 3
        finished = False
        numbers = []
        while not finished:
            module = input % 10
            division = int(input / 10)
            numbers.append(module)
            finished = division == 0
            input = division
        #ordenar de mayor a menor 3,4,1
        #obtener el texto y juntarlo
        is_special = numbers[1]*10 + numbers[0]
        if 10 < is_special < 20:
            ending_number = number_constants[input]
        elif 19 < is_special < 100:
            ending_number = ' '.join([
                number_constants[numbers[1]*10],
                number_constants[numbers[0]]
            ])

        # one hundred fourty three
        return number_constants[input]
