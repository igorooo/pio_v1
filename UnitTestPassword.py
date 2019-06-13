import pandas as pd

def unitTest(password):
    Errors = []

    length = len(password)
    result = True
    lengthError = 'Password is too short'
    capitalError = 'There is not enought capital letters in password'
    lowerError = 'There is not enought lower letters in password'
    digitError = 'There is not enought digits in password'
    signError = 'There is not enought signs in password'

    l_capital = l_lower = l_digits = l_signs = 0

    for c in password:
        if c.isupper():
            l_capital += 1
        if c.islower():
            l_lower += 1
        if c.isdigit():
            l_digits += 1
        if not c.isalnum():
            l_signs += 1

    if length < 8:
        result = False
        Errors.append(lengthError)
    if l_capital < 2:
        result = False
        Errors.append(capitalError)
    if l_lower < 2:
        result = False
        Errors.append(lowerError)
    if l_digits < 1:
        result = False
        Errors.append(digitError)
    if l_signs < 1:
        result = False
        Errors.append(signError)

    errs = str(int(result))

    if len(Errors) > 0:
        errs += ' -> '


    for com in Errors:
        errs = errs + com
        if Errors[-1] != com:
            errs += ', '

    return errs


if __name__ == '__main__':
    exc = pd.read_excel('unittest.xlsx')

    results = []

    for i in exc.index:
        print(exc['haslo'][i])
        results.append(unitTest(exc['haslo'][i]))

    print(results)





    print(unitTest('qa&uJjj'))
