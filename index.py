from number_constants import number_constants




def number_to_string(input):
    work_number = input
    word = ""
    while work_number != 0:
        tempword = ""
        if work_number >= 1000000:
            temp = work_number // 1000000
            tempword = number_to_string(temp)
            tempword = tempword + " " + number_constants[1000000]
            temp = temp * 1000000
            work_number = work_number - temp
        elif work_number >= 1000:
            temp = work_number // 1000
            tempword = number_to_string(temp)
            tempword = tempword + " " + number_constants[1000]
            temp = temp * 1000
            work_number = work_number - temp
        elif work_number >= 100:
            temp = work_number // 100
            tempword = number_to_string(temp)
            tempword = tempword + " " + number_constants[100]
            temp = temp * 100
            work_number = work_number - temp
        elif 100 > work_number > 20:
            temp = work_number // 10
            temp = temp * 10
            if len(tempword)>0:
                tempword = tempword + " " + number_constants[temp]
            else:
                tempword = number_constants[temp]
            work_number = work_number - temp
        elif work_number <= 20:
            if len(tempword)>0:
                tempword = tempword + " " + number_constants[work_number]
            else:
                tempword = number_constants[work_number]
            work_number = 0
        word = word + " " + tempword
    return word.strip()




