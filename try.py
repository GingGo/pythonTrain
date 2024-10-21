import ageAge

try:
    num = "qsqs"
    ageAge.enter_age(num)
except ageAge.NegativeNumberException as err:
    print(err)
except:
    print("Something we don't know error")
