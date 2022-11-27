import re


def validate_cnp_regex(cnp):
    cnp_regex = re.compile(r'^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0['
                           r'1-9]\d|[1-9]\d{2})\d$')
    return cnp_regex.match(cnp) is not None


def validate_cnp_last_digit(cnp):
    if len(cnp) != 13:
        return False

    cnp_arr = [*cnp]
    cnp_arr = list(map(int, cnp_arr))
    cnp_constant = [*"279146358279"]
    cnp_constant = list(map(int, cnp_constant))

    cnp_sum = 0
    for i in range(0, 12):
        cnp_sum += cnp_arr[i] * cnp_constant[i]

    cnp_sum = cnp_sum % 11

    if cnp_sum == 10:
        cnp_sum = 1

    return cnp_sum == cnp_arr[12]


def validate_cnp(cnp):
    return validate_cnp_regex(cnp) and validate_cnp_last_digit(cnp)