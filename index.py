from number_constants import number_constants
from time import sleep

def number_to_string(input):
    try:
        if input == 0:
            return "zero"
        input = abs(input)
        if (0 < input and input <= 20) and (input in number_constants):
            return number_constants[input]
        else:
            sOutput = ""
            sInput = str(input)
            counter = 0
            lenght = len(sInput)
            skip = False
            if lenght >= 3 and int(sInput[-2::]) in number_constants:
                counter = 2
                sOutput = number_to_string(int(sInput[-2::]))
                for digit in reversed(sInput[:-2]):
                    if skip:
                        skip = False
                        continue
                    if digit == '0':
                        counter += 1
                        continue
                    tenMult = pow(10,counter)
                    digit = int(digit)
                    if counter % 3 == 0 and tenMult in number_constants:
                        if counter < lenght:
                            if (sInput[(lenght-counter-2):(lenght-counter)]):
                                if int(sInput[(lenght-counter-2):(lenght-counter)]) in number_constants:
                                    if tenMult == 1:
                                        sOutput = f"{number_constants[int(sInput[(lenght-counter-2):(lenght-counter)])]} {sOutput}"
                                    else:
                                        sOutput = f"{number_constants[int(sInput[(lenght-counter-2):(lenght-counter)])]} {number_constants[tenMult]} {sOutput}"
                                    counter += 2
                                    skip = True
                                    continue
                        if tenMult == 1:
                            sOutput = f"{number_to_string(digit)} {sOutput}"
                        else:
                            sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                    elif counter % 3 == 0:
                        if counter % 6 > 2:
                            sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                        else:
                            sOutput = f"{number_to_string(digit)} {sOutput}"
                    elif counter % 3 == 1:
                        sOutput = f"{number_constants[digit*10]} {sOutput}"
                    elif counter % 3 == 2 and tenMult in number_constants:
                        sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                    else:
                        sOutput = f"{number_to_string(digit*100)} {sOutput}"
                    counter += 1
            else:
                for digit in reversed(sInput):
                    if skip:
                        skip = False
                        continue
                    if digit == '0':
                        counter += 1
                        continue
                    tenMult = pow(10,counter)
                    digit = int(digit)
                    if counter % 3 == 0 and tenMult in number_constants:
                        if counter < lenght:
                            if (sInput[(lenght-counter-2):(lenght-counter)]):
                                if int(sInput[(lenght-counter-2):(lenght-counter)]) in number_constants:
                                    if tenMult == 1:
                                        sOutput = f"{number_constants[int(sInput[(lenght-counter-2):(lenght-counter)])]} {sOutput}"
                                    else:
                                        sOutput = f"{number_constants[int(sInput[(lenght-counter-2):(lenght-counter)])]} {number_constants[tenMult]} {sOutput}"
                                    counter += 2
                                    skip = True
                                    continue
                        if tenMult == 1:
                            sOutput = f"{number_to_string(digit)} {sOutput}"
                        else:
                            sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                    elif counter % 3 == 0:
                        if counter % 6 > 2:
                            sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                        else:
                            sOutput = f"{number_to_string(digit)} {sOutput}"
                    elif counter % 3 == 1:
                        sOutput = f"{number_constants[digit*10]} {sOutput}"
                    elif counter % 3 == 2 and tenMult in number_constants:
                        sOutput = f"{number_to_string(digit)} {number_constants[tenMult]} {sOutput}"
                    else:
                        sOutput = f"{number_to_string(digit*100)} {sOutput}"
                    counter += 1
            return sOutput.strip()
    except:
        return "Input is not a valid number"

#5 148 121 123
number_to_string(5148121123)

