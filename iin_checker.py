import datetime

# mathmatical calculation for controlling digit
def calculation(iin_list, n_list):
    last_digit = 0
    for j in range(len(iin_list)):
        last_digit += int(iin_list[j]) * n_list[j]
    return last_digit % 11

def controlling_digit(arr, my_list, last_num):
    num = calculation(arr, my_list)
    
    if num == last_num:
        return True
    elif num == 10:
        del my_list[0]
        del my_list[1]
        my_list.append(1), my_list.append(2)
        ans = calculation(arr, my_list)
        if ans == last_num:
            return True
            # if calculation still returns 10 -> return invalid iin
        elif ans == 10:
            return False
        else:
            return False
    else:
        return False

def date_check(year, month, day):
    try:
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

def validity_iin(iin):
    # if iin contains non-integer value -> return invalid iin
    try:
        int(iin)
        # check for iin length
        if len(iin) != 12:
            return False

        year = iin[0:2]
        month = iin[2:4]
        day = iin[4:6]
        validity = date_check(year, month, day)

        if validity == False:
            return False

        today = datetime.date.today()
        year_current, month_current, day_current = str(today).split('-')
        new = day_current[0:2]
        new_year = year_current[2:4]
        iin_date = datetime.datetime(int(year), int(month), int(day))
        current_date = datetime.datetime(int(new_year), int(month_current), int(new))

        # check for currency considering 7-th digit
        if int(iin[6]) in range(5, 7): # here is the limitation: for 21 century it works fine, but we should also consider the further centuries(for the future)
            if current_date < iin_date:
                return False
        elif int(iin[6]) not in range(1, 5):
            return False
        # 1 -> man from 19 century    2 -> woman from 19th century   3 -> man from 20 century  4 -> woman from 20 century
        # 5 -> man from 21 century  6 -> woman from 21 century

        # check for last digit
        arr = [i for i in iin]
        del arr[-1]
        my_list = [i for i in range(1, 12)]
        control = controlling_digit(arr, my_list, int(iin[-1]), "IIN")
        return control
    except ValueError:
        return False

def validity_bin(bin):
    try:
        int(bin)

        if len(bin) != 12:
            return False

        if int(bin[4]) not in range(4, 7):
            return False
        
        if int(bin[5]) not in range(0, 4):
            return False

        year = bin[0:2]
        month = bin[2:4]
        validity = date_check(year, month, 1)

        if validity == False:
            return False

        # check for last digit
        arr = [i for i in bin]
        del arr[-1]
        my_list = [i for i in range(1, 12)]
        control = controlling_digit(arr, my_list, int(bin[-1]), "BIN")
        return control

    except ValueError:
        return False